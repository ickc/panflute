"""
Panflute: pandoc filters made simple
====================================

Panflute is a Python package that makes `Pandoc <http://pandoc.org/>`_
filters easier to write. (`Installation <install.html>`_)
"""

# from .utils import check_type, check_group, encode_dict

from .containers import ListContainer, DictContainer

from .base import Element, Block, Inline, MetaValue

from .elements import (
    Doc, Citation, TableRow, TableCell, ListItem, DefinitionItem, Definition)

from .elements import (
    Null, HorizontalRule, Space, SoftBreak, LineBreak, Str,
    Code, BlockQuote, Note, Div, Plain, Para, Emph, Strong, Strikeout,
    Superscript, Subscript, SmallCaps, Span, RawBlock, RawInline, Math,
    CodeBlock, Link, Image, BulletList, OrderedList, DefinitionList, Header,
    Quoted, Cite, Table)

from .elements import (
    MetaList, MetaMap, MetaString, MetaBool, MetaInlines, MetaBlocks)

from .io import load, dump, run_filter, run_filters
from .io import toJSONFilter, toJSONFilters  # Wrappers

from .tools import (
    stringify, yaml_filter, shell, convert_text, debug)

from .version import __version__