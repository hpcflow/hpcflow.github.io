---
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

## Stable ({{ latest_binary_tag_stable }})

Release notes: [link](https://github.com/hpcflow/hpcflow-new/releases/tag/{{ latest_binary_tag_stable }})
<table>
{% assign stable_bins = site.data.latest_binaries_stable[latest_binary_tag_stable] | sort %}
{% for binary in stable_bins %}  
  <tr>
    <td>{% assign exe_split = binary[0] | split: '-' %}{{ exe_split[-1] }}</td>
    <td><a href="{{ binary[1] }}">{{ binary[0] }}</a></td>
  </tr>
{% endfor %}
</table>

## Pre-release ({{ latest_binary_tag_pre_release }})

Release notes: [link](https://github.com/hpcflow/hpcflow-new/releases/tag/{{ latest_binary_tag_pre_release }})
<table>
{% assign pre_bins = site.data.latest_binaries_pre_release[latest_binary_tag_pre_release] | sort %}
{% for binary in pre_bins %}  
  <tr>
    <td>{% assign exe_split = binary[0] | split: '-' %}{{ exe_split[-1] }}</td>
    <td><a href="{{ binary[1] }}">{{ binary[0] }}</a></td>
  </tr>
{% endfor %}
</table>

## All releases

<ul>
{% for binary in site.data.all_binaries %}
  <li><a href="https://github.com/hpcflow/hpcflow-new/releases/tag/{{ binary[0] }}">{{ binary[0] }}</a></li>
{% endfor %}
</ul>
