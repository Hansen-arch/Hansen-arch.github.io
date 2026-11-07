# Reihan's Portfolio

This is the repository for my portfolio website, published at https://hansen-arch.github.io/

Built with:

* MkDocs and the Material theme
* GitHub Pages (the `gh-pages` branch)

Every page traces back to a real source document. The map of page to source is in
[`PORTFOLIO-SOURCES.md`](PORTFOLIO-SOURCES.md).

## Build and publish

```bash
# from the repo root, with the portfolio env active (.venv or conda env "portfolio")
mkdocs build        # writes site/, which is ignored by git
mkdocs gh-deploy    # rebuilds and pushes to the gh-pages branch
```

There is no GitHub Actions workflow in this repository, so pushing to `main` does not
publish anything. `mkdocs gh-deploy` is the only publish step.

> Tip: You can get the portfolio template from [Spatial Thoughts](https://github.com/spatialthoughts/portfolio-website-template)