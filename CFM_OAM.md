# CFM Protocol OAM Commands

## Retrieve lbm series output

### Description
This macro retrieves lbm series test output.

### Prerequisites
- CFM maintenance domain and group must be created.
- lbm series test must be completed.

### Altiplano Macro
**Macro ID:** `unicast-protocols-cfm-lbm-series-retrieve`

### Parameters
| Name                  | Type | Description                                                    | Optional | Examples |
|-----------------------|------|----------------------------------------------------------------|----------|----------|
| **maintenance-group-id** | str  | The maintenance group provides a handle for the MD and MA combination. | No       | MG       |
| **mep-id**              | int  | The MEP Id of the loopback message initiator.                 | No       | 8191     |

### vCLI Example
unicast-protocols-cfm-lbm-series-retrieve device-id <device> maintenance-group-id MG mep-id 8191

### Lightspan RPC
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="1">
  <get>
    <filter type="subtree">
      <cfm xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-cfm">
        <maintenance-group>
          <maintenance-group-id>MG</maintenance-group-id>
          <mep>
            <mep-id>8191</mep-id>
            <loopback-transmit-session xmlns="http://www.nokia.com/Fixed-Networks/BBA/yang/nokia-ieee802-dot1q-cfm-loopback-aug"/>
          </mep>
        </maintenance-group>
      </cfm>
    </filter>
  </get>
</rpc>

## Retrieve linktrace output
### Description
This macro retrieves linktrace series test output.

#### Prerequisites
- CFM maintenance domain and group must be created.
- linktrace test must be completed.

### Altiplano macro
**Macro id:** unicast-protocols-cfm-linktrace-retrieve

### Parameters
| Name                  | Type | Description                                                    | Optional | Examples |
|-----------------------|------|----------------------------------------------------------------|----------|----------|
| **maintenance-group-id** | str  | The maintenance group provides a handle for the MD and MA combination. | No       | MG       |
| **mep-id**              | int  | The MEP Id of the loopback message initiator.                 | No       | 8191     |

### vCLI Example
unicast-protocols-cfm-linktrace-retrieve device-id <device> maintenance-group-id MG mep-id 8191

### Lightspan RPC
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="1">
  <get>
    <filter type="subtree">
      <cfm xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-cfm">
        <maintenance-group>
          <maintenance-group-id>MG</maintenance-group-id>
          <mep>
            <mep-id>8191</mep-id>
            <linktrace-reply/>
          </mep>
        </maintenance-group>
      </cfm>
    </filter>
  </get>
</rpc>

## Initiate Linktrace Series Test

### Description
This macro initiates the linktrace series test.

### Prerequisites
- CFM maintenance domain and group must be created along with MEP.

### Altiplano Macro
**Macro ID:** `unicast-protocols-cfm-linktrace-series-action`

### Parameters
| Name                  | Type | Description                                                    | Optional | Examples               |
|-----------------------|------|----------------------------------------------------------------|----------|------------------------|
| **maintenance-group-id** | str  | The maintenance group provides a handle for the MD and MA combination. | No       | MG                    |
| **mep-id**              | int  | The MEP Id of the linktrace message initiator.                | No       | 8191                  |
| **target-mac-address**  | str  | The target MAC address field to be transmitted. A unicast MAC address. | No       | 00-00-00-97-00-07     |
| **ltm-ttl**             | int  | The LTM TTL field. Indicates the number of hops remaining to the LTM. | Yes      | 25                    |
| **ltm-flags**           | str  | The flags field for the LTMs transmitted by the MEP.          | Yes      | use-fdb-only          |

### vCLI Example
unicast-protocols-cfm-linktrace-series-action device-id <device> maintenance-group-id MG mep-id 8191 target-mac-address 00-00-00-97-00-07 ltm-ttl 25 ltm-flags use-fdb-only

### Lightspan RPC
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="1">
  <action xmlns="urn:ietf:params:xml:ns:yang:1">
    <cfm xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-cfm">
      <maintenance-group>
        <maintenance-group-id>MG</maintenance-group-id>
        <mep>
          <mep-id>8191</mep-id>
          <transmit-linktrace>
            <ltm-target-mac-address>00-00-00-97-00-07</ltm-target-mac-address>
            <ltm-ttl>25</ltm-ttl>
            <ltm-flags>use-fdb-only</ltm-flags>
          </transmit-linktrace>
        </mep>
      </maintenance-group>
    </cfm>
  </action>
</rpc>

## Initiate Loopback-Abort Test

### Description
This macro initiates the abort of the loopback series test.

### Prerequisites
- CFM maintenance domain and group must be created along with MEP.
- lbm originator test must be initiated and ongoing.

### Altiplano Macro
**Macro ID:** `unicast-protocols-cfm-loopback-abort-action`

### Parameters
| Name                  | Type | Description                                                    | Optional | Examples |
|-----------------------|------|----------------------------------------------------------------|----------|----------|
| **maintenance-group-id** | str  | The maintenance group provides a handle for the MD and MA combination. | No       | MG       |
| **mep-id**              | int  | The MEP Id of the loopback message initiator.                 | No       | 8191     |

### vCLI Example
unicast-protocols-cfm-loopback-abort-action device-id <device> maintenance-group-id MG mep-id 8191

### Lightspan RPC
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="1">
  <action xmlns="urn:ietf:params:xml:ns:yang:1">
    <cfm xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-cfm">
      <maintenance-group>
        <maintenance-group-id>MG</maintenance-group-id>
        <mep>
          <mep-id>8191</mep-id>
          <abort-loopback-series xmlns="http://www.nokia.com/Fixed-Networks/BBA/yang/nokia-ieee802-dot1q-cfm-loopback-aug"/>
        </mep>
      </maintenance-group>
    </cfm>
  </action>
</rpc>

## Initiate Loopback-Discover Test

### Description
This macro initiates the loopback discover test.

### Prerequisites
- CFM maintenance domain and group must be created along with MEP.

### Altiplano Macro
**Macro ID:** `unicast-protocols-cfm-loopback-discover-action`

### Parameters
| Name                  | Type | Description                                                                 | Optional | Examples |
|-----------------------|------|-----------------------------------------------------------------------------|----------|----------|
| **maintenance-group-id** | str  | The maintenance group provides a handle for the MD and MA combination.        | No       | MG       |
| **mep-id**              | int  | The MEP Id of the loopback message initiator.                                | No       | 8191     |
| **inner-tag-priority**   | int  | Priority. 3-bit value to be used in the inner tag, if present in the transmitted frame. | Yes      | 7        |
| **outer-tag-priority**   | int  | Priority. 3-bit value to be used in the outer tag, if present in the transmitted frame. | Yes      | 7        |

### vCLI Example
unicast-protocols-cfm-loopback-discover-action device-id <device> maintenance-group-id MG mep-id 8191 inner-tag-priority 7 outer-tag-priority 7

### Lightspan RPC
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="1">
  <action xmlns="urn:ietf:params:xml:ns:yang:1">
    <cfm xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-cfm">
      <maintenance-group>
        <maintenance-group-id>MG</maintenance-group-id>
        <mep>
          <mep-id>8191</mep-id>
          <transmit-loopback-discover xmlns="http://www.nokia.com/Fixed-Networks/BBA/yang/nokia-ieee802-dot1q-cfm-loopback-aug">
            <inner-tag-priority>7</inner-tag-priority>
            <outer-tag-priority>7</outer-tag-priority>
          </transmit-loopback-discover>
        </mep>
      </maintenance-group>
    </cfm>
  </action>
</rpc>

## Initiate Loopback-Series Test

### Description
This macro initiates the loopback series test.

### Prerequisites
- CFM maintenance domain and group must be created along with MEP.

### Altiplano Macro
**Macro ID:** `unicast-protocols-cfm-loopback-series-action`

### Parameters
| Name                     | Type | Description                                                                                                                                            | Optional | Examples               |
|--------------------------|------|--------------------------------------------------------------------------------------------------------------------------------------------------------|----------|------------------------|
| **maintenance-group-id**    | str  | The maintenance group provides a handle for the MD and MA combination.                                                                                   | No       | MG                    |
| **mep-id**                 | int  | The MEP Id of the loopback message initiator.                                                                                                           | No       | 8191                  |
| **dest-ucast-mac-address** | str  | The target unicast MAC Address field to be transmitted. A unicast destination MAC address.                                                              | No       | 00-00-00-97-00-07     |
| **message-interval**       | int  | Interval between the two LBM messages.                                                                                                                 | Yes      | 10                    |
| **inner-tag-priority**     | int  | Priority. 3-bit value to be used in the inner tag, if present in the transmitted frame.                                                                 | Yes      | 7                     |
| **inner-tag-drop-eligible**| bool | Specifies the value of the Drop Eligible Indicator (DEI) to be used in the inner tag, if present in the transmitted CFM packets.                        | Yes      | True                  |
| **outer-tag-priority**     | int  | Priority. 3-bit value to be used in the outer tag, if present in the transmitted frame.                                                                 | Yes      | 7                     |
| **outer-tag-drop-eligible**| bool | Specifies the value of the Drop Eligible Indicator (DEI) to be used in the outer tag, if present in the transmitted CFM packets.                        | Yes      | True                  |
| **data-tlv**               | str  | An arbitrary amount of data to be included in the Data TLV, if the Data TLV is selected to be sent. The input should be in base64 encoding format.      | Yes      | Tk9LSUFOT0tJQU5PS0lB  |
| **tlv-length**             | int  | The size of the data-tlv to be inserted in the LBM packet sent from our node. Indicates the total length of the TLV.                                    | Yes      | 64                    |
| **number-of-messages**     | int  | Number of LBM messages sent from DPU is defined as part of this field.                                                                                  | Yes      | 5                     |

### vCLI Example
unicast-protocols-cfm-loopback-series-action device-id <device> maintenance-group-id MG mep-id 8191 dest-ucast-mac-address 00-00-00-97-00-07 message-interval 10 inner-tag-priority 7 inner-tag-drop-eligible true outer-tag-priority 7 outer-tag-drop-eligible true data-tlv Tk9LSUFOT0tJQU5PS0lB tlv-length 64 number-of-messages 5

### Lightspan RPC
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="1">
  <action xmlns="urn:ietf:params:xml:ns:yang:1">
    <cfm xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-cfm">
      <maintenance-group>
        <maintenance-group-id>MG</maintenance-group-id>
        <mep>
          <mep-id>8191</mep-id>
          <transmit-loopback-series xmlns="http://www.nokia.com/Fixed-Networks/BBA/yang/nokia-ieee802-dot1q-cfm-loopback-aug">
            <lbm-dest-ucast-mac-address>00-00-00-97-00-07</lbm-dest-ucast-mac-address>
            <message-interval>10</message-interval>
            <vlan-tag-info>
              <inner-tag-priority>7</inner-tag-priority>
              <inner-tag-drop-eligible>true</inner-tag-drop-eligible>
              <outer-tag-priority>7</outer-tag-priority>
              <outer-tag-drop-eligible>true</outer-tag-drop-eligible>
            </vlan-tag-info>
            <pattern-tlv>
              <data-tlv>Tk9LSUFOT0tJQU5PS0lB</data-tlv>
              <tlv-length>64</tlv-length>
            </pattern-tlv>
            <number-of-messages>5</number-of-messages>
          </transmit-loopback-series>
        </mep>
      </maintenance-group>
    </cfm>
  </action>
</rpc>

## Remove CFM Maintenance Domain

### Description
This macro removes the CFM maintenance domain along with MA, MIP, and/or MEP.

### Prerequisites
- CFM maintenance domain configuration should be created.
- CFM maintenance group that references this maintenance domain should be deleted.

### Altiplano Macro
**Macro ID:** `unicast-protocols-cfm-md-remove`

### Parameters
| Name   | Type | Description                                            | Optional | Examples |
|--------|------|--------------------------------------------------------|----------|----------|
| **md-id** | str  | The Maintenance Domain name and name format choice. | No       | MD       |

### vCLI Example
unicast-protocols-cfm-md-remove device-id <device> md-id MD

### Lightspan RPC
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="1">
  <edit-config>
    <target>
      <running/>
    </target>
    <config>
      <cfm xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-cfm">
        <maintenance-domain xmlns:ns0="urn:ietf:params:xml:ns:netconf:base:1.0" ns0:operation="delete">
          <md-id>MD</md-id>
        </maintenance-domain>
      </cfm>
    </config>
  </edit-config>
</rpc>

## Retrieve CFM Maintenance Domain

### Description
This macro retrieves CFM maintenance domain profiles along with its MA, MIP, and/or MEP.

### Prerequisites
- CFM maintenance domain configuration should be created.

### Altiplano Macro
**Macro ID:** `unicast-protocols-cfm-md-retrieve`

### Parameters
| Name   | Type | Description                                            | Optional | Examples |
|--------|------|--------------------------------------------------------|----------|----------|
| **md-id** | str  | The Maintenance Domain name and name format choice. | No       | MD       |

### vCLI Example
unicast-protocols-cfm-md-retrieve device-id <device> md-id MD

### Lightspan RPC
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="1">
  <get-config>
    <source>
      <running/>
    </source>
    <filter type="subtree">
      <cfm xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-cfm">
        <maintenance-domain>
          <md-id>MD</md-id>
        </maintenance-domain>
      </cfm>
    </filter>
  </get-config>
</rpc>

## Remove CFM MEPs

### Description
This macro removes CFM MEPs.

### Prerequisites
- CFM maintenance group with MEPs must be created.

### Altiplano Macro
**Macro ID:** `unicast-protocols-cfm-mep-remove`

### Parameters
| Name                    | Type | Description                                                              | Optional | Examples |
|-------------------------|------|--------------------------------------------------------------------------|----------|----------|
| **maintenance-group-id** | str  | The maintenance group provides a handle for the MD and MA combination.   | No       | MG       |
| **mep-id**               | int  | The list of all MEPs that belong to this Maintenance Association.         | Yes      | 8191     |

### vCLI Example
unicast-protocols-cfm-mep-remove device-id <device> maintenance-group-id MG mep-id 8191

### Ligthspan RPC
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="1">
  <edit-config>
    <target>
      <running/>
    </target>
    <config>
      <cfm xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-cfm">
        <maintenance-group>
          <maintenance-group-id>MG</maintenance-group-id>
          <mep xmlns:ns0="urn:ietf:params:xml:ns:netconf:base:1.0" ns0:operation="delete">
            <mep-id>8191</mep-id>
          </mep>
        </maintenance-group>
      </cfm>
    </config>
  </edit-config>
</rpc>

## Configure CFM Maintenance Group

### Description
This macro creates a CFM maintenance group.

### Prerequisites
- CFM maintenance domain should be created (along with MIP and/or MEP).
- In case of using MIP, forwarder configurations must be created along with user and network VSI.

### Altiplano Macro
**Macro ID:** `unicast-protocols-cfm-mg-create`

### Parameters
| Name                       | Type | Description                                                                                                     | Optional | Examples     |
|----------------------------|------|-----------------------------------------------------------------------------------------------------------------|----------|--------------|
| **maintenance-group-id**   | str  | The maintenance group provides a handle for the MD and MA combination.                                          | No       | MG           |
| **md-id**                  | str  | The Maintenance Domain name and name format choice.                                                            | No       | MD           |
| **ma-id**                  | str  | The Maintenance Association name and name format choice.                                                       | No       | MA           |
| **mep-id**                 | int  | The list of all MEPs that belong to this Maintenance Association.                                               | Yes      | 8191         |
| **direction**              | str  | The direction in which the MEP faces on the Bridge Port.                                                       | No       | down, up     |
| **mep-state**              | bool | The administrative state of the MEP. TRUE indicates that the MEP is to function normally, FALSE indicates it is to cease functioning. | Yes      | True         |
| **interface**              | str  | References the interface on which the MEP shall be created.                                                    | No       | uni1_vsi1    |
| **forwarder**              | str  | All MIPs within a single MA shall reference VLAN sub-interfaces that participate in the same forwarder.         | Yes      | fwd_common   |
| **ccm-ltm-priority**       | str  | The priority value for CCMs and LTMs transmitted by the MEP. Default is the highest priority allowed for the MEP's VID(s). | Yes      | 3            |
| **ccm-ltm-inner-tag-priority** | str  | Priority (3-bit value) to be used in the inner tag, if present in the transmitted frame. Default is 7 if not configured. | Yes      | 3            |

### vCLI Example
unicast-protocols-cfm-mg-create device-id <device> maintenance-group-id MG md-id MD ma-id MA mep-id 8191 direction down mep-state true interface uni1_vsi1 forwarder fwd_common ccm-ltm-priority 3 ccm-ltm-inner-tag-priority 3

### Lightspan RPC
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="1">
  <edit-config>
    <target>
      <running/>
    </target>
    <config>
      <cfm xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-cfm">
        <maintenance-group>
          <maintenance-group-id>MG</maintenance-group-id>
          <md-id>MD</md-id>
          <ma-id>MA</ma-id>
          <mep>
            <mep-id>8191</mep-id>
            <direction>down</direction>
            <ccm-ltm-priority>3</ccm-ltm-priority>
            <ccm-ltm-inner-tag-priority xmlns="http://www.nokia.com/Fixed-Networks/BBA/yang/nokia-sdan-ieee802-dot1q-cfm-aug">3</ccm-ltm-inner-tag-priority>
            <enabled>true</enabled>
            <interface xmlns="urn:bbf:yang:bbf-oam-cfm-mp-to-interface">uni1_vsi1</interface>
          </mep>
          <forwarder xmlns="urn:bbf:yang:bbf-oam-cfm-ma-to-forwarder">fwd_common</forwarder>
        </maintenance-group>
      </cfm>
    </config>
  </edit-config>
</rpc>

## Remove CFM Maintenance Group

### Description
This macro removes a CFM maintenance group.

### Prerequisites
- CFM maintenance group must be created.

### Altiplano Macro
**Macro ID:** `unicast-protocols-cfm-mg-remove`

### Parameters
| Name                    | Type | Description                                                              | Optional | Examples |
|-------------------------|------|--------------------------------------------------------------------------|----------|----------|
| **maintenance-group-id** | str  | The maintenance group provides a handle for the MD and MA combination.   | No       | MG       |

### vCLI Example
unicast-protocols-cfm-mg-remove device-id <device> maintenance-group-id MG

### Lightspan RPC
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="1">
  <edit-config>
    <target>
      <running/>
    </target>
    <config>
      <cfm xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-cfm">
        <maintenance-group xmlns:ns0="urn:ietf:params:xml:ns:netconf:base:1.0" ns0:operation="delete">
          <maintenance-group-id>MG</maintenance-group-id>
        </maintenance-group>
      </cfm>
    </config>
  </edit-config>
</rpc>

## Retrieve CFM Maintenance Group

### Description
This macro retrieves the CFM maintenance group profile.

### Prerequisites
- CFM maintenance group configuration should be created.

### Altiplano Macro
**Macro ID:** `unicast-protocols-cfm-mg-retrieve`

### Parameters
| Name                    | Type | Description                                                              | Optional | Examples |
|-------------------------|------|--------------------------------------------------------------------------|----------|----------|
| **maintenance-group-id** | str  | The maintenance group provides a handle for the MD and MA combination.   | No       | MG       |

### vCLI Example
unicast-protocols-cfm-mg-retrieve device-id <device> maintenance-group-id MG

### Lightspan RPC
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="1">
  <get-config>
    <source>
      <running/>
    </source>
    <filter type="subtree">
      <cfm xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-cfm">
        <maintenance-group>
          <maintenance-group-id>MG</maintenance-group-id>
        </maintenance-group>
      </cfm>
    </filter>
  </get-config>
</rpc>

## Retrieve Local MEPs State Data and Statistics

### Description
This macro retrieves CFM maintenance group state-data and its counter details.

### Prerequisites
- CFM maintenance domain and group must be created.

### Altiplano Macro
**Macro ID:** `unicast-protocols-cfm-mg-mep-retrieve`

### Parameters
| Name                    | Type | Description                                                              | Optional | Examples |
|-------------------------|------|--------------------------------------------------------------------------|----------|----------|
| **maintenance-group-id** | str  | The maintenance group provides a handle for the MD and MA combination.   | No       | MG       |

### vCLI Example
unicast-protocols-cfm-mg-mep-retrieve device-id <device> maintenance-group-id MG

### Lightspan RPC
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="1">
  <get>
    <filter type="subtree">
      <cfm xmlns="urn:ieee:std:802.1Q:yang:ieee802-dot1q-cfm">
        <maintenance-group>
          <maintenance-group-id>MG</maintenance-group-id>
        </maintenance-group>
      </cfm>
    </filter>
  </get>
</rpc>

## Retrieve Interface-State CFM Stack Details

### Description
This macro retrieves interface state CFM stack details.

### Prerequisites
- CFM maintenance domain and group must be created.

### Altiplano Macro
**Macro ID:** `unicast-protocols-cfm-stack-retrieve`

### Parameters
| Name       | Type | Description                 | Optional | Examples |
|------------|------|-----------------------------|----------|----------|
| **md-level** | int  | The Maintenance Domain level. | Yes      | 0        |

### vCLI Example
unicast-protocols-cfm-stack-retrieve device-id <device> md-level 0

### Lightspan RPC
<rpc xmlns="urn:ietf:params:xml:ns:netconf:base:1.0" message-id="1">
  <get>
    <filter type="subtree">
      <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
        <interface>
          <cfm-stack xmlns="http://www.nokia.com/Fixed-Networks/BBA/yang/nokia-ieee802-dot1q-cfm-stack-aug">
            <cfm-stack>
              <md-level>0</md-level>
            </cfm-stack>
          </cfm-stack>
        </interface>
      </interfaces-state>
    </filter>
  </get>
</rpc>


