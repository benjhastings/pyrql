# -*- coding: utf-8 -*-

from pyrql.exceptions import RQLSyntaxError
from pyrql.parser import Parser
from pyrql.unparser import Unparser
from pyrql.query import Query


__title__ = 'pyrql'
__version__ = '0.4.0'
__author__ = 'Pedro Werneck'
__license__ = 'MIT'


parse = Parser().parse

unparse = Unparser().unparse

query = Query().query


__all__ = ['parse', 'unparse', 'query', 'RQLSyntaxError']
