# KicadModTree is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# KicadModTree is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with kicad-footprint-generator. If not, see < http://www.gnu.org/licenses/ >.
#
# (C) 2018 by Thomas Pointhuber, <thomas.pointhuber@gmx.at>

from KicadModTree.PolygonPoints import *
from KicadModTree.Point import *
from KicadModTree.nodes.Node import Node


class Polygon(Node):
    r"""Add a Polygon to the render tree

    :param \**kwargs:
        See below

    :Keyword Arguments:
        * *polygon* (``list(Point)``) --
          outer nodes of the polygon
        * *layer* (``str``) --
          layer on which the line is drawn (default: 'F.SilkS')
        * *width* (``float``) --
          width of the line (default: None, which means auto detection)

    :Example:

    >>> from KicadModTree import *
    >>> Polygon(nodes=[[-2, 0], [0, -2], [4, 0], [0, 2]], layer='F.SilkS')
    """

    def __init__(self, **kwargs):
        Node.__init__(self)
        self.nodes = PolygonPoints(**kwargs)

        self.layer = kwargs.get('layer', 'F.SilkS')
        self.width = kwargs.get('width')

    def calculateBoundingBox(self):
        return nodes.calculateBoundingBox()

    def _getRenderTreeText(self):
        render_text = Node._getRenderTreeText(self)
        render_text += " [nodes: ["

        node_strings = []
        for n in self.nodes:
            node_strings.append("[x: {x}, y: {y}]".format(x=n.x, y=n.y))

        if len(node_strings) <= 6:
            render_text += ", ".join(node_strings)
        else:
            # display only a few nodes of the beginning and the end of the polygone line
            render_text += ", ".join(node_strings[:3])
            render_text += ",... , "
            render_text += ", ".join(node_strings[-3:])

        render_text += "]"

        return render_text

    def cut(self, other):
        r""" Cut other polygon from this polygon

        More details see PolygonPoints.cut docstring.

        :param other: the other polygon
        """
        self.nodes.cut(other.nodes)
