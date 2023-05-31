#!/usr/bin/env python3
# Show documentation for Terraform resource or datasource in the terminal
import sys
from typing import Callable
import requests
import re
import webbrowser
import urllib.parse
from rich.console import Console
from rich.markdown import Markdown

# Shortcut types
#   a -
#   b -
#   c -
#   d - data source
#   e - expression
#   f - function
#   g - google
#   h -
#   i -
#   j -
#   k -
#   l -
#   m - meta-arguments
#   n -
#   o -
#   p -
#   q -
#   r - resource
#   s -
#   t -
#   u -
#   v -
#   w -
#   x -
#   y -
#   z -


def build_url(*parts):
    return f"https://{'/'.join(parts)}"


def _lookup_direct(url_parts: list[str]) -> Callable[[], str]:
    def lookup(*_) -> str:
        response = requests.get(build_url(*url_parts))
        response.raise_for_status()
        return response.text

    return lookup


def _lookup_provider_official_legacy(
    provider: str,
    ghorg: str = "hashicorp",
    ghbranch: str = "main",
    subdir: str = "website/docs",
    thing_prefix: str = "",
    file_extension: str = ".html.markdown",
) -> Callable[[str, str], str]:
    def lookup(thing_type: str, thing: str) -> str:
        thing_type = thing_type[0].lower()
        response = requests.get(
            build_url(
                "raw.githubusercontent.com",
                ghorg,
                f"terraform-provider-{provider}",
                ghbranch,
                subdir,
                thing_type,
                f"{thing_prefix}{thing}{file_extension}",
            )
        )
        response.raise_for_status()
        return response.text

    return lookup


def _lookup_provider_tfplugindocs(
    provider: str,
    ghorg: str = "hashicorp",
    ghbranch: str = "main",
    subdir: str = "docs",
    thing_prefix: str = "",
    file_extension: str = ".md",
) -> Callable[[str, str], str]:
    def lookup(thing_type: str, thing: str) -> str:
        thing_path = {
            "r": "resources",
            "d": "data-sources",
        }.get(thing_type[0].lower())
        response = requests.get(
            build_url(
                "raw.githubusercontent.com",
                ghorg,
                f"terraform-provider-{provider}",
                ghbranch,
                subdir,
                thing_path,
                f"{thing_prefix}{thing}{file_extension}",
            )
        )
        response.raise_for_status()
        return response.text

    return lookup


def _lookup_platform(doc_path: str, ghbranch: str = "main", subdir: str = "website/docs") -> Callable[[str], str]:
    def lookup(thing: str) -> str:
        if not thing:
            thing = "index"
        # hacky special case for `index` function
        if doc_path == "language/functions" and thing == "index":
            thing = "index_function"
        response = requests.get(
            f"https://raw.githubusercontent.com/hashicorp/terraform/{ghbranch}/{subdir}/{doc_path}/{thing}.mdx"
        )
        response.raise_for_status()
        return response.text

    return lookup


lookup_special_provider_functions = {
    "external": _lookup_direct([
        "raw.githubusercontent.com",
        "hashicorp",
        "terraform-provider-external",
        "main",
        "docs",
        "data-sources",
        "external.md",
    ]),
    "http": _lookup_direct([
        "raw.githubusercontent.com",
        "hashicorp",
        "terraform-provider-http",
        "main",
        "docs",
        "data-sources",
        "http.md",
    ]),
}

lookup_provider_functions = {
    "ad": _lookup_provider_tfplugindocs(provider="ad"),
    "alicloud": _lookup_provider_official_legacy(provider="alicloud", ghorg="aliyun", ghbranch="master"),
    "archive": _lookup_provider_tfplugindocs(provider="archive"),
    "aws": _lookup_provider_official_legacy(provider="aws"),
    "awscc": _lookup_provider_tfplugindocs(provider="awscc"),
    "azuread": _lookup_provider_tfplugindocs(provider="azuread"),
    "azurerm": _lookup_provider_official_legacy(provider="azurerm"),
    "azurestack": _lookup_provider_official_legacy(provider="azurestack"),
    "boundary": _lookup_provider_tfplugindocs(provider="boundary"),
    "ciscoasa": _lookup_provider_official_legacy(provider="ciscoasa", ghorg="CiscoDevNet", ghbranch="master"),
    "cloudflare": _lookup_provider_tfplugindocs(provider="cloudflare", ghorg="cloudflare", ghbranch="master"),
    "cloudinit": _lookup_provider_tfplugindocs(provider="cloudinit"),
    "consul": _lookup_provider_tfplugindocs(provider="consul", ghbranch="master"),
    "datadog": _lookup_provider_tfplugindocs(provider="datadog", ghorg="DataDog", ghbranch="master"),
    "dns": _lookup_provider_tfplugindocs(provider="dns"),
    "github": _lookup_provider_official_legacy(provider="github", ghorg="integrations"),
    "google": _lookup_provider_official_legacy(provider="google"),
    "googleworkspace": _lookup_provider_tfplugindocs(provider="googleworkspace"),
    "hcp": _lookup_provider_tfplugindocs(provider="hcp"),
    "hcs": _lookup_provider_tfplugindocs(provider="hcs"),
    "helm": _lookup_provider_official_legacy(provider="helm"),
    "kubernetes": _lookup_provider_official_legacy(provider="kubernetes"),
    "lacework": _lookup_provider_official_legacy(provider="lacework", ghorg="lacework"),
    "launchdarkly": _lookup_provider_official_legacy(provider="launchdarkly", ghorg="launchdarkly"),
    "libvirt": _lookup_provider_official_legacy(provider="libvirt", ghorg="dmacvicar"),
    "local": _lookup_provider_tfplugindocs(provider="local"),
    "netbox": _lookup_provider_tfplugindocs(provider="netbox", ghorg="e-breuninger", ghbranch="master", file_extension=".md"),
    "nomad": _lookup_provider_official_legacy(provider="nomad"),
    "null": _lookup_provider_tfplugindocs(provider="null"),
    "oci": _lookup_provider_official_legacy(provider="oci", ghorg="terraform-providers", ghbranch="master"),
    "opc": _lookup_provider_official_legacy(provider="opc", ghorg="terraform-providers", ghbranch="master", thing_prefix="opc_"),
    "oraclepaas": _lookup_provider_official_legacy(provider="oraclepaas", ghorg="terraform-providers", ghbranch="master", thing_prefix="oraclepaas_"),
    "random": _lookup_provider_tfplugindocs(provider="random"),
    "salesforce": _lookup_provider_tfplugindocs(provider="salesforce"),
    "tfe": _lookup_provider_official_legacy(provider="tfe"),
    "time": _lookup_provider_tfplugindocs(provider="time"),
    "tls": _lookup_provider_tfplugindocs(provider="tls"),
    "twingate": _lookup_provider_tfplugindocs(provider="twingate", ghorg="Twingate"),
    "vault": _lookup_provider_official_legacy(provider="vault", file_extension=".html.md"),
    "vsphere": _lookup_provider_official_legacy(provider="vsphere"),
}

lookup_platform_functions = {
    "e": _lookup_platform(doc_path="language/expressions"),
    "f": _lookup_platform(doc_path="language/functions"),
    "m": _lookup_platform(doc_path="language/meta-arguments"),
}


def main():
    console = Console(color_system="256")
    if "-h" in sys.argv:
        console.print("Usage: tfman {type} {thing}")
        console.print("  Example: tfman r aws_instance")
        sys.exit(0)
    use_pager = False
    if "-p" in sys.argv:
        use_pager = True
    full_name = sys.argv[-1]
    thing_type = sys.argv[-2]
    short_thing_type = thing_type[0]
    if short_thing_type in ("g"):
        q = f"terraform {full_name}"
        console.print(f'Googling "{q}"...')
        webbrowser.open(f"https://google.com/search?q={urllib.parse.quote_plus(q)}")
        sys.exit(0)
    elif short_thing_type in ("d", "r"):
        # Some special cases
        if full_name in lookup_special_provider_functions.keys():
            lookup_function = lookup_special_provider_functions[full_name]
            doc = lookup_function()
        else:
            provider, thing = re.findall(r"(\w+?)_(.*)", full_name)[0]
            lookup_function = lookup_provider_functions.get(provider, None)
            if lookup_function == None:
                raise Exception(f"Provider {provider} not supported.")
            doc = lookup_function(thing_type, thing)
    elif short_thing_type in lookup_platform_functions.keys():
        lookup_function = lookup_platform_functions.get(short_thing_type, None)
        if lookup_function == None:
            raise Exception(f"Platform type {thing_type} not supported.")
        doc = lookup_function(full_name)
    else:
        raise Exception(f"dunno what {thing_type} is")
    md = Markdown(doc)
    if use_pager:
        with console.pager():
            console.print(md)
    else:
        console.print(md)


if __name__ == "__main__":
    main()
