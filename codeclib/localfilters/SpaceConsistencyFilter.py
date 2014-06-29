"""
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from codeclib.fillib import LocalFilter
from codeclib.fillib.results.LineResult import LineResult
from codeclib.fillib.util import IndentationHelper
from codeclib.fillib.util.settings import Settings


class SpaceConsistencyFilter(LocalFilter.LocalFilter):

    def run(self, filename, file):
        results = []
        filtername = "SpaceConsistencyFilter"
        assert isinstance(self.settings, Settings)

        use_spaces = bool(self.settings["usespaces"].value[0])
        tab_width = int(self.settings["tabwidth"].value[0])
        indent_helper = IndentationHelper.IndentationHelper(tab_width)

        for line_number, line in enumerate(file):
            indentation, rest, count = indent_helper.get_indentation(line)
            if use_spaces and indentation.find("\t") >= 0:
                results.append(LineResult(filename,
                                          filtername,
                                          "Line contains one or more tabs",
                                          line_number+1,
                                          line,
                                          ' '*count + rest))

        return results

    @staticmethod
    def get_needed_settings():
        return {"TabWidth" : "Number of spaces to display for a tab",
                "UseSpaces": "True if spaces are to be used, false for tabs"}
