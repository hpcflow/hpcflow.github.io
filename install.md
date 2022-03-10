---
layout: default
---

There are two methods to using hpcflow: via a binary executable file or via a Python package. Both methods allow the design and execution of workflows. If you want to use hpcflow on a cluster, using the binary executable file is recommended. If you want to design and explore your workflows using the Python API, then you need the Python package. You can use both simultaneously if you wish!

# Install Python package

**Using pip**

`pip install hpcflow`

**Using conda**

`conda -c conda_forge install hpcflow`

# Download binaries

<ul>
{% for binary in site.data.binaries %}
  <li>{{ binary[0] }}</li>
{% endfor %}
</ul>

## Stable

## Development

## Previous releases


# Install hpcflow

`pip install hpcflow`
