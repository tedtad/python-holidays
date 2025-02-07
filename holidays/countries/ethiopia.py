# -*- coding: utf-8 -*-

#  python-holidays
#  ---------------
#  A fast, efficient Python library for generating country, province and state
#  specific sets of holidays on the fly. It aims to make determining whether a
#  specific date is a holiday as fast and flexible as possible.
#
#  Author:  ryanss <ryanssdev@icloud.com> (c) 2014-2017
#           dr-prodigy <maurizio.montel@gmail.com> (c) 2017-2021
#  Website: https://github.com/dr-prodigy/python-holidays
#  License: MIT (see LICENSE file)

from datetime import date
#from calendar import isleap
from dateutil.easter import easter
from dateutil.relativedelta import relativedelta as rd
from holidays.constants import SAT,SUN
from holidays.constants import JAN,MAR, MAY,SEP
from holidays.holiday_base import HolidayBase
from holidays.utils import islamic_to_gre

WEEKEND = (SAT,SUN)


class Ethiopia(HolidayBase):
  # Holidays here are estimates, it is common for the day to be pushed
  # if falls in a weekend, although not a rule that can be implemented.
  # Holidays after 2020: the following four moving date holidays whose exact
  # date is announced yearly are estimated (and so denoted):
  # - Eid El Fetr*
  # - Eid El Adha*
  # - Arafat Day*
  # - Moulad El Naby*
  # *only if hijri-converter library is installed, otherwise a warning is
  #  raised that this holiday is missing. hijri-converter requires
  #  Python >= 3.6
  # is_weekend function is there, however not activated for accuracy.

  def __init__(self, **kwargs):
    self.country = "ET"
    HolidayBase.__init__(self, **kwargs)

  def _populate(self, year):
    # New Year's Day
    #The Ethiopian New Year is called Kudus Yohannes in Ge'ez and Tigrinya, while in Amharic, 
    # the official language of Ethiopia it is called Enkutatash. 
    # It occurs on September 11 in the Gregorian Calendar; 
    # except for the year preceding a leap year, when it occurs on September 12.
    if self.ethiopian_isleap(year):
      self[date(year, SEP, 12)] = "አዲስ ዓመት እንቁጣጣሽ/Ethiopian New Year"
    else:
      self[date(year, SEP, 11)] = "አዲስ ዓመት እንቁጣጣሽ/Ethiopian New Year"

    # Finding of true cross
    if self.ethiopian_isleap(year):
      self[date(year, SEP, 28)] = "መስቀል/Finding of True Cross"
    else:
      self[date(year, SEP, 27)] = "መስቀል/Finding of True Cross"

    # Ethiopian Christmas
    self[date(year, JAN, 7)] = "ገና/Ethiopian X-Mas"

    # Ethiopian Ephiphany
    self[date(year, JAN, 19)] = "ጥምቀት/Ephiphany"

    # Ethiopian Good Friday
    self[easter(year, 2) - rd(days=2)] = "ስቅለት/Ethiopian Good Friday"

    # Ethiopian  Easter - Orthodox Easter
    self[easter(year, 2)] = "ፋሲካ/Ethiopian Easter"

    # Adwa Victory Day
    if year > 1896:
      self[date(year, MAR, 2)] = "አድዋ/Victory of Adwa"

    # Labour Day
    self[date(year, MAY, 1)] = "የሰራተኞች ቀን/Labor Day"

    # Patriots Day
    if year > 1941:
      self[date(year, MAY, 5)] = "የአርበኞች ቀን/Patriots Day"

    # Derg Downfall Day
    if year > 1991:
      self[date(year, MAY, 28)] = "ደርግ የወደቀበት ቀን/Downfall of Dergue regime"

    # Downfall of King. Hailesilassie
    if year < 1991 and year > 1974 :
      if self.ethiopian_isleap(year):
        self[date(year, SEP, 13)] = "ደርግ የመጣበት ቀን/Formation of Dergue"
      else:
        self[date(year, SEP, 12)] = "ደርግ የመጣበት ቀን/Formation of Dergue"
    # Eid al-Fitr - Feast Festive
    # date of observance is announced yearly, This is an estimate since
    # having the Holiday on Weekend does change the number of days,
    # deceided to leave it since marking a Weekend as a holiday
    # wouldn't do much harm.
    for date_obs in islamic_to_gre(year, 10, 1):
      hol_date = date_obs
      self[hol_date ] = "ኢድ አልፈጥር/Eid-Al-Fitr"

    # Eid al-Adha - Scarfice Festive
    # date of observance is announced yearly
    for date_obs in islamic_to_gre(year, 12, 9):
      hol_date = date_obs
      self[hol_date + rd(days=1)] = "አረፋ/Eid-Al-Adha"

    # Prophet Muhammad's Birthday - (hijari_year, 3, 12)
    for date_obs in islamic_to_gre(year, 3, 12):
      hol_date = date_obs
      self[hol_date+ rd(days=1)] = "መውሊድ/Prophet Muhammad's Birthday"

# the Ethiopian leap years have coincided with leap years in the Gregorian calendar 
# until the end of February 2100. It starts earlier from new year of western calander
# Ethiopian leap year start on Sep 11, therefore it has an effect on holidays b/n
# Sep 11 and Jan 1. Therfore, here on the following function we intentionally add 1 to the leap year to offset the difference

  def ethiopian_isleap(self, year):
    year = year+1 
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

class ET(Ethiopia):
  pass


class ETH(Ethiopia):
  pass
