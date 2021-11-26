# analyze-google-ads

Meltano project [file bundle](https://meltano.com/docs/command-line-interface.html#file-bundle) of Matatika datasets for Google Ads. These datasets are automatically added to your Matatika workspace when you initialize a Google Ads pipeline.

Files:
- [`analyze/datasets`](./bundle/analyze/datasets) (directory)

### Adding this file bundle to your own Meltano project

Add plugin to `discovery.yml`:
```yaml
files:
- name: analyze-google-ads
  namespace: tap_google_ads
  repo: https://github.com/Matatika/analyze-google-ads
  pip_url: git+https://github.com/Matatika/analyze-google-ads.git
```

Add plugin to your Meltano project:
```bash
# Add only the file bundle
meltano add files analyze-google-ads

# Add the file bundle as a related plugin through adding the Google Ads extractor
meltano add extractor --include-related tap-google-ads
```
