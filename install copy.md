<!-- ---
layout: default
---

{% include get_latest_binaries.html type="stable" %}
{% assign latest_binary_tag_stable = latest_binary_tag %}

{% include get_latest_binaries.html type="pre_release" %}
{% assign latest_binary_tag_pre_release = latest_binary_tag %}

There are two methods to using hpcflow: via a binary executable file or via a Python package. Both methods allow the design and execution of workflows. If you want to use hpcflow on a cluster, using the binary executable file is recommended. If you want to design and explore your workflows using the Python API, then you need the Python package. You can use both simultaneously if you wish!

# Install Python package

**Using pip**

`pip install hpcflow`

**Using conda**

`conda -c conda_forge install hpcflow`

# Download binaries

## Stable ({% latest_binary_tag_stable %})

<ul>
{% for binary in site.data.latest_binaries_stable.latest_binary_tag_stable %}
  <li>{{ binary[0] }}</li>
{% endfor %}
</ul>

## Pre-release  ({% latest_binary_tag_pre_release %})
<ul>
{% for binary in site.data.latest_binaries_pre_release.latest_binary_tag_pre_release %}
  <li>{{ binary[0] }}</li>
{% endfor %}
</ul>

## Development

## Previous releases

<ul>
{% for binary in site.data.all_binaries %}
  <li>{{ binary[0] }}</li>
{% endfor %}
</ul>

# Install hpcflow

`pip install hpcflow` -->
