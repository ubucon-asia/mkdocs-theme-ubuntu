# MkDocs Ubuntu Theme

A MkDocs Theme build with [Vanilla framework](https://vanillaframework.io/)

## Using this theme

Simply set theme property in `mkdocs.yml` as follows

```yml
...
theme:
    name: ubuntu
```

It's also required to set `site_name_short` for title in header. And `repo_name` for hyperlink label of your repository URL.

```yml
site_name: MkDocs Ubuntu Theme
site_name_short: Ubuntu Theme # Title for header
...

repo_url: https://github.com/ubucon-asia/mkdocs-theme-ubuntu
repo_name: ubucon-asia/mkdocs-theme-ubuntu # For hyperlink label on footer
```