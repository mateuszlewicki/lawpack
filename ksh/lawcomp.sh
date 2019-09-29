#!/bin/env ksh
# TODO: set as on HP-UX

# NAME: lawcomp
# AUTHOR: Mateusz Lewicki - ATOS - mateusz.lewicki@atos.net
# DESCRIPTION: 
#	lawcomp is script which is taking care of program compilation and error checking.
# 	script is using build-in commands as qcompile, scrgen, genformap, and so on. For
# 	description of used commands please refer to man pager or to third-party documentation
#



declare s_conf=true
declare package=$1
declare code=${package::2}
declare lawdir=$LAWDIR
declare pdl=$XXPDL
declare src_cat=$lawdir'/'$pdl




#	 show_conf()
#	 print used config

function show_conf() {

	printf 'Your config: \n %s:%s\n%s:%s\n%s:%s\n%s:%s\n' "Package" "${package}" "Lawson directory" "${lawdir}" "Product Line" "${pdl}" "Sources catalog" "${src_cat}"

}


#	hand_err()
#	Check if last return code is other than zero
#	if it is non-zero code print message then exit

function hand_err() {
	if [ ! $? ]
	then
		printf '[ ERROR ] Application occured no-zero return code %d at stage %s\n exiting' "$(echo -n $1)" ${1:-"Not Specified"}
		exit 1
	fi
}

#	hand_comp_err()
#	Check if $package.err file is present in src catalog
#	if it is present print error message, show last lines 
# 	and exit


function hand_comp_err() {
	if [ -e ${src_cat}'/'${code}'src/'${package}'.err' ]
	then
		print '[ ERROR ] { COMPILATION EXCEPTION }  \n %s \n exiting' "$(tail ${src_cat}'/'${code}'src/'${package}'.err')" 
		exit 2
	fi
}

# 	main()
#	main script logic

function main() {
	
#	if $s_conf - Show config - variable is setted true
#	print config and ask user for acceptance

	if $s_conf 
	then
		show_conf
		read -p "Do you agree?" 
		
		# if user entered nN - simply not agreed - exit the script 

		if $REPLY == "n" || $REPLY == "N" 
		then
			exit 3
		fi
	fi
	#Start compilation of $package at $pdl
	$(qcomplie $pdl $code $package)
	hand_err "Start Compilation"

	# TODO qstatus
	# check if program is still in the queue


	hand_comp_err
	# execute scrgen	
	$(scrgen $pdl $code $package)
	hand_err "scrgen"

	# execute genformap 
	$(genformap SCHLUM2 $pdl $code $package)
	hand_err "genformap"

	# print ending message
	printf 'All Task ended succesfully \n' 
	
	
}
