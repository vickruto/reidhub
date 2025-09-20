import re

def on_page_markdown(markdown, page, config, **kwargs):
    """
    Rewrite HTML <... src="../..."> paths so they resolve correctly
    in the built MkDocs site. Markdown image syntax is untouched.
    """
    url = (page.url or "").strip("/")
    segments = [s for s in url.split("/") if s]
    up = "../" * len(segments)

    # Rewrite all src="../..." cases
    markdown = re.sub(
        r'src=(["\'])\.\./',
        rf'src=\1{up}',
        markdown
    )
    return markdown
