"""Wrap pint to pretend that we are not implementation-specific."""

from pint import UnitRegistry as _UnitRegistry
units = _UnitRegistry()
