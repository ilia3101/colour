# -*- coding: utf-8 -*-
"""
Blackmagic Colourspaces
============================

Defines the *Blackmagic* colourspaces:

-   :attr:`colour.models.BMD_FILM_V1_COLOURSPACE`.
-   :attr:`colour.models.BMD_4K_FILM_V1_COLOURSPACE`.
-   :attr:`colour.models.BMD_4K_FILM_V3_COLOURSPACE`.
-   :attr:`colour.models.BMD_46K_FILM_V1_COLOURSPACE`.
-   :attr:`colour.models.BMD_46K_FILM_V3_COLOURSPACE`.
-   :attr:`colour.models.BMD_WIDE_GAMUT_V4_COLOURSPACE`.

References
----------
-   :cite:`Blackmagic2020a` : Blackmagic Design. (2020). DaVinci Resolve
    CIE Chromaticity Plot.
"""

from __future__ import division, unicode_literals

import numpy as np

from colour.colorimetry import ILLUMINANTS
from colour.models.rgb import (RGB_Colourspace, log_encoding_BMDFilm,
                               log_decoding_BMDFilm, log_encoding_BMD4KFilm,
                               log_decoding_BMD4KFilm, log_encoding_BMD46KFilm,
                               log_decoding_BMD46KFilm,
                               log_encoding_BMDPocket4KFilmV4,
                               log_decoding_BMDPocket4KFilmV4,
                               log_encoding_BMDPocket6KFilmV4,
                               log_decoding_BMDPocket6KFilmV4,
                               normalised_primary_matrix)

__author__ = 'Colour Developers'
__copyright__ = 'Copyright (C) 2013-2020 - Colour Developers'
__license__ = 'New BSD License - https://opensource.org/licenses/BSD-3-Clause'
__maintainer__ = 'Colour Developers'
__email__ = 'colour-developers@colour-science.org'
__status__ = 'Production'

__all__ = [
    'BMD_FILM_V1_PRIMARIES', 'BMD_FILM_V1_WHITEPOINT_NAME',
    'BMD_FILM_V1_WHITEPOINT', 'BMD_FILM_V1_TO_XYZ_MATRIX',
    'XYZ_TO_BMD_FILM_V1_MATRIX', 'BMD_FILM_V1_COLOURSPACE',
    'BMD_4K_FILM_V1_PRIMARIES', 'BMD_4K_FILM_V1_WHITEPOINT_NAME',
    'BMD_4K_FILM_V1_WHITEPOINT', 'BMD_4K_FILM_V1_TO_XYZ_MATRIX',
    'XYZ_TO_BMD_4K_FILM_V1_MATRIX', 'BMD_4K_FILM_V1_COLOURSPACE',
    'BMD_4K_FILM_V3_PRIMARIES', 'BMD_4K_FILM_V3_WHITEPOINT_NAME',
    'BMD_4K_FILM_V3_WHITEPOINT', 'BMD_4K_FILM_V3_TO_XYZ_MATRIX',
    'XYZ_TO_BMD_4K_FILM_V3_MATRIX', 'BMD_4K_FILM_V3_COLOURSPACE',
    'BMD_46K_FILM_V1_PRIMARIES', 'BMD_46K_FILM_V1_WHITEPOINT_NAME',
    'BMD_46K_FILM_V1_WHITEPOINT', 'BMD_46K_FILM_V1_TO_XYZ_MATRIX',
    'XYZ_TO_BMD_46K_FILM_V1_MATRIX', 'BMD_46K_FILM_V1_COLOURSPACE',
    'BMD_46K_FILM_V3_PRIMARIES', 'BMD_46K_FILM_V3_WHITEPOINT_NAME',
    'BMD_46K_FILM_V3_WHITEPOINT', 'BMD_46K_FILM_V3_TO_XYZ_MATRIX',
    'XYZ_TO_BMD_46K_FILM_V3_MATRIX', 'BMD_46K_FILM_V3_COLOURSPACE',
    'BMD_WIDE_GAMUT_V4_PRIMARIES', 'BMD_WIDE_GAMUT_V4_WHITEPOINT_NAME',
    'BMD_WIDE_GAMUT_V4_WHITEPOINT', 'BMD_WIDE_GAMUT_V4_TO_XYZ_MATRIX',
    'XYZ_TO_BMD_WIDE_GAMUT_V4_MATRIX', 'BMD_WIDE_GAMUT_V4_COLOURSPACE'
]

BMD_FILM_V1_PRIMARIES = np.array([
    [0.9173, 0.2502],
    [0.2833, 1.7072],
    [0.0856, -0.0708],
])
"""
*BMD Film V1* colourspace primaries.

BMD_FILM_V1_PRIMARIES : ndarray, (3, 2)
"""

BMD_FILM_V1_WHITEPOINT_NAME = 'BMD White'
"""
*BMD Film V1* colourspace whitepoint name.

BMD_FILM_V1_WHITEPOINT : unicode
"""

BMD_FILM_V1_WHITEPOINT = np.array([
    [0.3135, 0.3305],
])
"""
*BMD Film V1* colourspace whitepoint.

BMD_FILM_V1_WHITEPOINT : ndarray
"""

BMD_FILM_V1_TO_XYZ_MATRIX = (normalised_primary_matrix(
    BMD_FILM_V1_PRIMARIES, BMD_FILM_V1_WHITEPOINT))
"""
*BMD Film V1* colourspace to *CIE XYZ* tristimulus values matrix.

BMD_FILM_V1_TO_XYZ_MATRIX : array_like, (3, 3)
"""

XYZ_TO_BMD_FILM_V1_MATRIX = (
    np.linalg.inv(BMD_FILM_V1_TO_XYZ_MATRIX))
"""
*CIE XYZ* tristimulus values to *BMD Film V1* colourspace matrix.

XYZ_TO_BMD_FILM_V1_MATRIX : array_like, (3, 3)
"""

BMD_FILM_V1_COLOURSPACE = RGB_Colourspace(
    'BMD Film V1',
    BMD_FILM_V1_PRIMARIES,
    BMD_FILM_V1_WHITEPOINT,
    BMD_FILM_V1_WHITEPOINT_NAME,
    BMD_FILM_V1_TO_XYZ_MATRIX,
    XYZ_TO_BMD_FILM_V1_MATRIX,
    log_encoding_BMDFilm,
    log_decoding_BMDFilm,
)
BMD_FILM_V1_COLOURSPACE.__doc__ = """
*BMD Film V1* colourspace.

    References
    ----------
    :cite:`Blackmagic2020a`

BMD_FILM_V1_COLOURSPACE : RGB_Colourspace
"""