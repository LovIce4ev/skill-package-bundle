import requests
from bs4 import BeautifulSoup
import sys
import re


HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}


def fetch_article(url):
    response = requests.get(url, headers=HEADERS, timeout=30)
    response.raise_for_status()
    html_text = response.text
    soup = BeautifulSoup(html_text, 'html.parser')

    title_el = soup.find(id='activity-name')
    if title_el:
        title = title_el.text.strip()
    else:
        og_title = soup.find('meta', property='og:title')
        title = og_title['content'].strip() if og_title else 'No Title'

    content_el = soup.find(id='js_content')
    body = ''
    if content_el:
        body = extract_content(content_el)
    else:
        # Fallback for short posts / picture posts where content is in meta/JS
        og_desc = soup.find('meta', property='og:description')
        if og_desc and og_desc.get('content'):
            # Basic unescaping of WeChat's special encodings
            desc_text = og_desc['content'].replace('\\x0a', '<br>').replace('\\x26amp;', '&').replace('\\x26nbsp;', ' ')
            body += f'<p>{desc_text}</p>'
        
        # Extract images from JS specifically avoiding watermark and share_cover variants
        list_match = re.search(r'window\.picture_page_info_list\s*=\s*\[(.*?)\]\s*;', html_text, re.DOTALL)
        
        seen_urls = set()
        clean_urls = []
        if list_match:
            # specifically find the main cdn_url, which is cleanly indented by 6 spaces
            img_urls = re.findall(r"\n      cdn_url:\s*'([^']+)'", list_match.group(1))
            for u in img_urls:
                u = u.replace('\\/', '/').replace('\\x26amp;', '&')
                if u and u.startswith('http') and u not in seen_urls:
                    seen_urls.add(u)
                    clean_urls.append(u)
        else:
            # Fallback if window.picture_page_info_list is not present
            img_urls = re.findall(r"cdn_url[a-zA-Z0-9_]*:\s*(?:JsDecode\('([^']+)'\)|'([^']+)')", html_text)
            for match in img_urls:
                u = match[0] if match[0] else match[1]
                if u and u.startswith('http'):
                    u = u.replace('\\/', '/').replace('\\x26amp;', '&')
                    id_match = re.search(r'/([^/]+)/0(?:\?|$)', u)
                    if id_match:
                        file_id = id_match.group(1)
                        if file_id not in seen_urls:
                            seen_urls.add(file_id)
                            clean_urls.append(u)
                    else:
                        if u not in seen_urls:
                            seen_urls.add(u)
                            clean_urls.append(u)
        
        for u in clean_urls:
            body += f'<img src="{u}" />'

    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>{title}</title>
<style>
body {{ max-width: 800px; margin: 40px auto; padding: 0 20px; font-family: -apple-system, sans-serif; line-height: 1.8; }}
h1 {{ font-size: 24px; }}
img {{ max-width: 100%; height: auto; display: block; margin: 12px 0; }}
</style>
</head>
<body>
<h1>{title}</h1>
{body}
</body>
</html>"""
    return title, html


def extract_content(node):
    parts = []
    for child in node.children:
        if child.name is None:
            text = child.string
            if text and text.strip():
                parts.append(f'<p>{text.strip()}</p>')
        elif child.name == 'img':
            img_url = child.get('data-src') or child.get('src')
            if img_url:
                parts.append(f'<img src="{img_url}" />')
        elif child.name in ('br', 'hr'):
            parts.append(f'<{child.name} />')
        elif child.name in ('p', 'section', 'div', 'span', 'blockquote',
                            'ul', 'ol', 'li', 'h1', 'h2', 'h3', 'h4',
                            'strong', 'em', 'a'):
            inner = extract_content(child)
            if inner.strip():
                parts.append(f'<{child.name}>{inner}</{child.name}>')
        else:
            inner = extract_content(child)
            if inner.strip():
                parts.append(inner)
    return '\n'.join(parts)


if __name__ == '__main__':
    url = sys.argv[1] if len(sys.argv) > 1 else 'https://mp.weixin.qq.com/s/PcqfCz6rEeg1981VHymnPA'
    title, html = fetch_article(url)
    output = 'output.html'
    with open(output, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'Title: {title}')
    print(f'Saved to {output}')
