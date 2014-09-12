# -*- coding: utf-8 -*-
#
# Point Class Assigner Plugin
# Copyright (C) 2014 Peter Ersts
# ersts@amnh.org
#
# --------------------------------------------------------------------------
#
# This file is part of Point Class Assigner.
#
# Point Class Assigner is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# Point Class Assigner is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Point Class Assigner.  If not, see <http://www.gnu.org/licenses/>.
#
# This work was supported by Conservation International under grant  #66236,
# entitled Partnership on research on methods and strategies for monitoring
# selected non-forest habitats, awarded to the American Museum of Natural History,
# Center for Biodiversity and Conservation.
# --------------------------------------------------------------------------
"""
 This script initializes the plugin, making it known to QGIS.
"""

def classFactory(iface):
  from PointClassAssigner import PointClassAssigner
  return PointClassAssigner(iface)
