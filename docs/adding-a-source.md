# Adding a Source

To adapt this project, create one extractor per source.

Examples:

- `competitor_blog_extract.py`
- `github_releases_extract.py`
- `security_advisories_extract.py`
- `grant_opportunities_extract.py`

Each extractor should return:

- title
- url
- date
- source
- category
- score
- include
- reason

Run an extractor like this:

```bash
python3 extractors/examples/custom_topic_extract.py 2026-05-25 2026-05-31 --included-only
