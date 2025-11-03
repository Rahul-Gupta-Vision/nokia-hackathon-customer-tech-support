# CFM Debugging Session

## About
Ethernet CFM, a network-level Ethernet OAM mechanism, supports functions including end-to-end connectivity fault detection, fault advertisement, fault acknowledgement, and fault locations. CFM monitors network connectivity and pinpoints connectivity faults. It is used with protection switching techniques to make networks more reliable.

## CFM Terminologies

Maintenance Domain (MD) — An MD contains one or more MAs that have the same MD level.

Maintenance Association (MA) — A set of Maintenance endpoints (MEPs) that have the same maintenance domain (MD) level within one service instance. This includes both local and remote MEP’s.

MA Endpoint (MEP) — MEPs initiate and terminate CFM messages, and are the origination and termination points of the CFM operations. The MEP is identified by the MEP ID  and is unique within an MA.

MA Intermediate Point (MIP) — MIPs receive CFM messages and respond to the originating MEP. A MIP never initiates messages and does not expect any messages. MIPs respond to loopback and link trace messages.

Maintenance Association Group (MG) - The list of maintenance association groups, which are uniquely associated with a maintenance domain, maintenance association, for which the MEPs belong. Maintenance group provide support for configuring list of local MEPs.


## CFM Protocol Messages - Loopback Message ( LBM )

Used to verify the connectivity with another MEP or MIP
Similar to the PING command which helps to check whether a network element is reachable
On Demand operation
Bidirectional - The target MEP/MIP responds with LBR
Mostly Unicast loopback is used – MEP/MIP MAC will be the Destination Address.
ITU-T also supports multicast LBM – Class 1 (01:80:c2:00:00:3x, x=[0…7]) Multicast Destination Address.

## CFM Protocol Messages - Linktrace Message ( LTM )

Used to check the path from one MEP to another MEP or MIP
Similar to the TraceRoute command which helps to trace the path to a network element
On Demand operation
Multicast Class 2 DA (01:80:c2:00:00:3y, y=[8…F]) is used
All intermediate MPs respond with LTR
The destination MEP/MIP is identified by the “Target MAC Address” field
The LTM is forwarded on the Association till the Target MP is reached
The TTL field is used to set the maximum number of hops across which the LTM is forwarded


# Debugging

## Statistics
isam-reborn# show running-config cfm maintenance-domain
cfm maintenance-domain mD10_L0
 char-string mDomain_mD10_L0    ! DEFAULT
 md-level    0    ! 0
 maintenance-association mA100_mD10_L0
  char-string  mAssociation_mA100_mD10_L0
  mhf-creation mhf-default    ! mhf-none
  maintenance-association-mep 100
  !
 !
 maintenance-association mA101_mD10_L0
  char-string  mAssociation_mA101_mD10_L0
  mhf-creation mhf-default    ! mhf-none
  maintenance-association-mep 101
  !
 !
 maintenance-association mA102_mD10_L0
  char-string  mAssociation_mA102_mD10_L0
  mhf-creation mhf-default    ! mhf-none
  maintenance-association-mep 102
  !
 !
 maintenance-association mA103_mD10_L0
  char-string  mAssociation_mA103_mD10_L0
  mhf-creation mhf-default    ! mhf-none
  maintenance-association-mep 103
  !
 !

isam-reborn# show running-config cfm maintenance-group
cfm maintenance-group mG100_mD10_L0
 md-id     mD10_L0
 ma-id     mA100_mD10_L0
 forwarder fwd_S+C_RB_1504
 mep 100
  direction up
  enabled
  interface uni_vsi1504
 !
!
cfm maintenance-group mG100_mD10_L1
 md-id     mD10_L1
 ma-id     mA100_mD10_L1
 forwarder fwd_S+C_RB_1504
 mep 100
  direction up
  enabled
  interface uni_vsi1504
 !
!
cfm maintenance-group mG100_mD10_L2
 md-id     mD10_L2
 ma-id     mA100_mD10_L2
 forwarder fwd_S+C_RB_1504
 mep 100
  direction up
  enabled
  interface uni_vsi1504
 !
!


## T&D Commands

Enable Logging for CFM Application

>> logging module loglevel 1 7
>> logging module loglevel 2 7
>> logging module loglevel 4 7
>> logging module loglevel 7 7



>> CFM List
list registered commands for module [cfm]:
dump
show
counter
send
da

CFM dump Command
>> cfm dump help
available commands :
dump all : dumps all shared DB information
dump port all : dumps all the port's cfm information
dump cfm port <index> : dumps specified port's cfm information
dump mep stats <mg_id> <mep_id> : dumps Mep statistics for a given Mep ID
dump mg stats <mg_id> : dumps Mep statistics for a given MG ID
dump mac info <itf> : dump MAC address information for the given interface
dump capability : dump board-specific capabilities fetched from CRM
dump counters : dump all debug counters
dump fwd itfusg : dump all forwader LTM disard interface-usage info
dump oamrequests : dumps all oam requests with results

>> cfm dump port all
Dumps the cfm information for all interfaces


>> cfm dump cfm port 2
dumping for port 2 
Dumps the cfm information for the given interface 2


>> cfm dump mep stats 1 1

>> cfm dump mg stats 1

dump mac info <itf>



>> cfm dump capability
Number of auto mip creation supported interface types [2]
user-port
subtended-node-port

Number of cfm sub protocols supported [4]
LBR
LBM
LTR
LTM

Number of Max Ondemand Sessions [5]

Number of Max Ondemand McastSessions [2]

Number of Max Ondemand LTM Response [40]

Number of Max Ondemand Mcast LBM Response [40]



>> cfm dump counters
=== Protocol Thread ===

>> cfm dump fwd itfusg
Dumps the MG forwarder LTM Discard interface-usage
Forwarder info cache
Number of forwarders[2496]
Forwarder name[fwd_S+C_RB_1]
Forwarder index[0]
[8]MGs associated with forwarder[fwd_S+C_RB_1]
MD Level[0] MG Id[8633]

Forwarder name[fwd_S+C_RB_10]
Forwarder index[0]
[8]MGs associated with forwarder[fwd_S+C_RB_10]
MD Level[0] MG Id[1337]

Forwarder name[fwd_S+C_RB_100]
Forwarder index[0]
[8]MGs associated with forwarder[fwd_S+C_RB_100]
MD Level[0] MG Id[57]

Forwarder name[fwd_S+C_RB_1000]
Forwarder index[0]
[8]MGs associated with forwarder[fwd_S+C_RB_1000]
MD Level[0] MG Id[14953]

Forwarder name[fwd_S+C_RB_1001]
Forwarder index[0]
[8]MGs associated with forwarder[fwd_S+C_RB_1001]
MD Level[0] MG Id[15081]

Forwarder name[fwd_S+C_RB_1002]
Forwarder index[0]
[8]MGs associated with forwarder[fwd_S+C_RB_1002]
MD Level[0] MG Id[15209]

>> cfm dump oamrequests
+------OAM Active Requests(0)-------+

+------OAM Request - Results-------+

>> cfm show all pktsnooprules
LBM
PACKET_LEVEL DIR  MAC_TYPE          OPCODE   PKT_ACTION
ING_MEP      ING  UCAST_ITF_MAC     LBM      SNOOP
ING_MEP      ING  UCAST_NOT_ITF_MAC LBM      DISCARD
ING_MEP      ING  MCAST_CLASS1      LBM      SNOOP

LTM
PACKET_LEVEL DIR  MAC_TYPE          OPCODE   PKT_ACTION
ING_MEP      ING  UCAST_ITF_MAC     LTM      DISCARD
ING_MEP      ING  UCAST_NOT_ITF_MAC LTM      DISCARD
ING_MEP      ING  MCAST_CLASS1      LTM      DISCARD
ING_MEP      ING  MCAST_CLASS2      LTM      SNOOP

LBR
PACKET_LEVEL DIR  MAC_TYPE          OPCODE   PKT_ACTION
ING_MEP      ING  UCAST_ITF_MAC     LBR      SNOOP
ING_MEP      ING  UCAST_NOT_ITF_MAC LBR      DISCARD
ING_MEP      ING  MCAST_CLASS1      LBR      DISCARD
ING_MEP      ING  MCAST_CLASS2      LBR      DISCARD
ING_MEP      EGR  UCAST_ITF_MAC     LBR      DISCARD
ING_MEP      EGR  UCAST_NOT_ITF_MAC LBR      DISCARD
ING_MEP      EGR  MCAST_CLASS1      LBR      DISCARD
ING_MEP      EGR  MCAST_CLASS2      LBR      DISCARD
EGR_MEP      ING  UCAST_ITF_MAC     LBR      DISCARD
EGR_MEP      ING  UCAST_NOT_ITF_MAC LBR      DISCARD
EGR_MEP      ING  MCAST_CLASS1      LBR      DISCARD
EGR_MEP      ING  MCAST_CLASS2      LBR      DISCARD
EGR_MEP      EGR  UCAST_ITF_MAC     LBR      SNOOP

LTR
PACKET_LEVEL DIR  MAC_TYPE          OPCODE   PKT_ACTION
ING_MEP      ING  UCAST_ITF_MAC     LTR      SNOOP
ING_MEP      ING  UCAST_NOT_ITF_MAC LTR      DISCARD
ING_MEP      ING  MCAST_CLASS1      LTR      DISCARD
ING_MEP      ING  MCAST_CLASS2      LTR      DISCARD

>> cfm show lbm pktsnooprules
dumping lbm rules

>> cfm show ltm pktsnooprules
dumping ltm rules
PACKET_LEVEL DIR  MAC_TYPE          OPCODE   PKT_ACTION


>> cfm show lbr pktsnooprules
dumping lbr rules

>> cfm show ltr pktsnooprules
dumping ltr rules

>> cfm counter reset

>> cfm send lbm 18:4A:6F:5F:9C:9A 0
sending lbm with given destination mac and level

>> cfm send ltm 18:4A:6F:5F:9C:9A 0
sending ltm with given destination mac and level

>> cfm send frame lbm 0
sending given lbm frame

>> cfm send frame ltm 0
sending given ltm frame

>> cfm da dump
Number of entries tracked  [59904]
Number of invalid entries  [0]
Number of conflict entries [0]
Number of mismatch entries [0]
Number of active entries   [0]
-----------------
Request-ID -- CMD
-----------------
-----------------

>> cfm da clear
request-list cleared
>> cfm da dump
Number of entries tracked  [0]
Number of invalid entries  [0]
Number of conflict entries [0]
Number of mismatch entries [0]
Number of active entries   [0]
-----------------
Request-ID -- CMD
-----------------
-----------------


