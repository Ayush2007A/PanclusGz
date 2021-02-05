PanclusGz is the panclus version for the next the older version named Panclus which was not the best but it was very useful in calculating the dates of solar and lunar eclipses as well as in converting speech to text in any language and with the translation of the text.PanclusGz comes with all these features and also have more attributes as well as some sub-modules.
# Usage for PanclusGz:

# Sub-Modules 
1. [locations](https://github.com/Ayush2007A/PanclusGz/blob/main/locations.py)<br>
2. [dependencies](https://github.com/Ayush2007A/PanclusGz/blob/main/locations.py)<br>
3. [Gz](https://github.com/Ayush2007A/PanclusGz/blob/main/Gz.py)<br>
4. [Installer](https://github.com/Ayush2007A/PanclusGz/blob/main/Installer.py)<br>

# locations:
	from PanclusGz import locations as ls
	# To find the weather of any place
	ls.get_weather('India')
	
	# To get area of any country
	ls.area("India")

	# To get full info of the country
	ls.full_info('India')
	
	# To find the capital of any country
	ls.capital('India')
	
	# To find the country code
	ls.country_code('India')
	
# Gz:
	from PanclusGz import Gz as gz
	# For converting text to speech
	gz.speak('hello')
	
	# To make it speak in several languages
	
	# This is the format
	
	gz.speak_in_language(text_to_speak,language_code,name_of_file_to_save)
	
	gz.speak_in_language('hello','en-Us','test.mp3')
	
	# To search wikipedia
	gz.wikit('what is python')

	# To search on google
	gz.search('python')

	# To find solar or Lunar eclipse date
	gz.date_solar_eclipse()
	gz.date_lunar_eclipse()

	# To copy paste text
	gz.copy('hello')
	gz.paste()

	# To see date and time
	gz.show_date()
	gz.show_time()

	# To translate text
	gz.translate(from_language,to_language,text_of_translation)
	gz.translate('english','hindi','hello')

	# To open a file from system
	gz.openfile('cmd')

# Installer:
Installer is a basic app to install python packages
	from PanclusGz import Installer

# Dependencies:
It is used to see dependencies of the package
	
	from PanclusGz import dependencies 
