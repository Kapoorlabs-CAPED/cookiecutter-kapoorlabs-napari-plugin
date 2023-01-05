{% if cookiecutter.use_git_tags_for_versioning == 'y' %}
try:
    from ._version import version as __version__
except ImportError:
    __version__ = "unknown"
{% else -%}
__version__ = "0.0.1"
{% endif -%}

{% if cookiecutter.include_reader_plugin == 'y' %}
from ._reader import napari_get_reader
{% endif %}{% if cookiecutter.include_sample_data_plugin == 'y' -%}
from ._sample_data import make_sample_data
{% endif %}{% if cookiecutter.include_widget_plugin == 'y' -%}
from ._widget import plugin_wrapper_track
{% endif %}{% if cookiecutter.include_writer_plugin == 'y' -%}
from ._writer import write_multiple, write_single_image
{% endif %}
from ._temporal_plots import TemporalStatistics 
from ._table_widget import TrackTable
from ._data_model import pandasModel

__all__ = (
    {% if cookiecutter.include_reader_plugin == 'y' -%}
    "napari_get_reader",
    {% endif %}{% if cookiecutter.include_writer_plugin == 'y' -%}
    "write_single_image",
    "write_multiple",
    {% endif %}{% if cookiecutter.include_sample_data_plugin == 'y' -%}
    "make_sample_data",
    {% endif %}{% if cookiecutter.include_widget_plugin == 'y' -%}
    "plugin_wrapper_track",
    "TemporalStatistics",
    "TrackTable",
    "pandasModel"
{% endif -%}
)
