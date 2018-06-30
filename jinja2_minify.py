#
# Jinja2-Minify
#
# Copyright (C) 2018 Boris Raicheff
# All rights reserved
#


from cssmin import cssmin
from htmlmin import minify
from jinja2 import nodes
from jinja2.ext import Extension
from jsmin import jsmin


class HTMLMinExtension(Extension):

    tags = {'htmlmin'}

    def parse(self, parser):
        lineno = next(parser.stream).lineno
        body = parser.parse_statements(['name:endhtmlmin'], drop_needle=True)
        return nodes.CallBlock(self.call_method('_minify'), [], [], body).set_lineno(lineno)

    @staticmethod
    def _minify(caller):
        return minify(
            caller(),
            remove_comments=True,
            reduce_boolean_attributes=True,
            remove_optional_attribute_quotes=False
        ).strip()


class CSSMinExtension(Extension):

    tags = {'cssmin'}

    def parse(self, parser):
        lineno = next(parser.stream).lineno
        body = parser.parse_statements(['name:endcssmin'], drop_needle=True)
        return nodes.CallBlock(self.call_method('_minify'), [], [], body).set_lineno(lineno)

    @staticmethod
    def _minify(caller):
        return cssmin(caller()).strip()


class JSMinExtension(Extension):

    tags = {'jsmin'}

    def parse(self, parser):
        lineno = next(parser.stream).lineno
        body = parser.parse_statements(['name:endjsmin'], drop_needle=True)
        return nodes.CallBlock(self.call_method('_minify'), [], [], body).set_lineno(lineno)

    @staticmethod
    def _minify(caller):
        return jsmin(caller()).strip()


# EOF
