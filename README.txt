# Srimalaya Ladha

Description:
- test_kb.txt contains rules for setup of an office space
- The idea is that when all components are present, your office is successfully setup
- This may be a useful tool in finding out what components are missing and
	for learning how to setup a full-fledged office

Office:
- All the essential things for a perfect office are mentioned (about 40 rules are present)

EXAMPLE RUN:
kb> load test_kb.txt
	office <-- infrastructure & staff & database & retail_centre & safety
	infrastructure <-- building & furniture & utilities & parking
	computer <-- hardware & os & power
	hardware <-- memory & ports & io_devices
	ports <-- usb & charging & auxiliary
	memory <-- ram & rom
	io_devices <-- display & keyboard & mouse & audio
	audio <-- speaker & mic
	network <-- ethernet & wifi & contact & mail & server
	equipment <-- printer & scanner & stationary & computer
	furniture <-- couch & chair & desk
	stationary <-- pens & pencils & stapler & shredder
	waiting_area <-- coffee & catalogues & lounge
	lounge <-- couch & chair
	rooms <-- workspace & conference_room & waiting_area & locker
	workspace <-- computer & equipment
	conference_room <-- projector & desk & camera & chair
	utilities <-- water & washroom & kitchen & recreation & cleaning
	staff <-- receptionist & manager & employee & technician
	contact <-- email & telephone
	database <-- files & folders & repositories & library
	mail <-- letters & parcels & deliveries
	library <-- books & catalogues & lounge
	locker <-- lock & id
	recreation <-- games & television
	games <-- billiards & ping_pong & console
	circulation <-- aisles & bullpen
	building <-- floor & rooms & circulation & ventilation
	ventilation <-- windows & ducts & air_conditioning
	retail_centre <-- products & sales & pos
	server <-- backup & collaboration
	safety <-- security & emergency_exit & first_aid
	security <-- security_office & surveillance
	security_office <-- security_personnel & restraints & safety_equipment
	surveillance <-- camera & patrol
	emergency_exit <-- stairs & outdoor_ladder & service_entrance
	first_aid <-- medical_kit & bandages & ointments
	medical_kit <-- antiseptic_cleaner & pain_killers & ice_packs
	cleaning <-- garbage & mops & cleaners
	parking <-- garage & permit & street

	40 new rule(s) added
kb> infer_all
	Newly inferred atoms:
	   <none>
	Atoms already known to be true:
	   <none>
kb> tell io_devices hardware audio
	"hardware" added to KB
	"io_devices" added to KB
	"audio" added to KB
kb> tell hardware
	atom "hardware" already known to be true
kb> infer_all
	Newly inferred atoms:
	   <none>
	Atoms already known to be true:
	   hardware, io_devices, audio
kb> tell ram rom os power
	"os" added to KB
	"power" added to KB
	"ram" added to KB
	"rom" added to KB
kb> infer_all
	Newly inferred atoms:
	   computer, memory
	Atoms already known to be true:
	   hardware, io_devices, audio, os, power, ram, rom
kb> infer_all
	Newly inferred atoms:
	   <none>
	Atoms already known to be true:
	   hardware, io_devices, audio, os, power, ram, rom, computer, memory
kb>
