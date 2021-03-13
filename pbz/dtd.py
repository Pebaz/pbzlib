"""
<!-- EXAMPLE DTD -->
<!ELEMENT NOTE (
    TO,
    FROM?,
    (HEADING+, BODY*),
    (PS | PPS)
)>
<!ELEMENT TO (#PCDATA)>
<!ELEMENT FROM (#PCDATA)>
<!ELEMENT HEADING (#PCDATA)>
<!ELEMENT BODY (#PCDATA)>
<!ELEMENT PS (#PCDATA)>
<!ELEMENT PPS (#PCDATA)>
"""

import re, pprint, collections

"""
<!-- QUALYS KNOWLEDGE_BASE_VULN_LIST_OUTPUT DTD -->
<!ELEMENT KNOWLEDGE_BASE_VULN_LIST_OUTPUT (REQUEST?,RESPONSE)>
<!ELEMENT REQUEST (DATETIME, USER_LOGIN, RESOURCE, PARAM_LIST?,
POST_DATA?)>
<!ELEMENT DATETIME (#PCDATA)>
<!ELEMENT USER_LOGIN (#PCDATA)>
<!ELEMENT RESOURCE (#PCDATA)>
<!ELEMENT PARAM_LIST (PARAM+)>
<!ELEMENT PARAM (KEY, VALUE)>
<!ELEMENT KEY (#PCDATA)>
<!ELEMENT VALUE (#PCDATA)>
<!-- if returned, POST_DATA will be urlencoded -->
<!ELEMENT POST_DATA (#PCDATA)>
<!ELEMENT RESPONSE (DATETIME, (VULN_LIST|ID_SET)?, WARNING?)>
<!-- DATETIME already defined -->
<!ELEMENT VULN_LIST (VULN*)>
<!ELEMENT VULN (QID, VULN_TYPE, SEVERITY_LEVEL, TITLE, CATEGORY?,
    DETECTION_INFO?, LAST_CUSTOMIZATION?,
    LAST_SERVICE_MODIFICATION_DATETIME?, PUBLISHED_DATETIME,
    BUGTRAQ_LIST?, PATCHABLE, SOFTWARE_LIST?, VENDOR_REFERENCE_LIST?,
    CVE_LIST?, DIAGNOSIS?, DIAGNOSIS_COMMENT?, CONSEQUENCE?,
    CONSEQUENCE_COMMENT?, SOLUTION?, SOLUTION_COMMENT?, COMPLIANCE_LIST?,
    CORRELATION?, CVSS?, CVSS_V3?, PCI_FLAG?, AUTOMATIC_PCI_FAIL?,
    PCI_REASONS?, THREAT_INTELLIGENCE?, SUPPORTED_MODULES?, DISCOVERY,
    IS_DISABLED?, CHANGE_LOG_LIST? )>
<!ELEMENT QID (#PCDATA)>
<!ELEMENT VULN_TYPE (#PCDATA)>
<!ELEMENT SEVERITY_LEVEL (#PCDATA)>
<!ELEMENT TITLE (#PCDATA)>
<!ELEMENT CATEGORY (#PCDATA)>
<!ELEMENT DETECTION_INFO (#PCDATA)>
<!ELEMENT LAST_CUSTOMIZATION (DATETIME, USER_LOGIN?)>
<!ELEMENT LAST_SERVICE_MODIFICATION_DATETIME (#PCDATA)>
<!ELEMENT PUBLISHED_DATETIME (#PCDATA)>
<!ELEMENT BUGTRAQ_LIST (BUGTRAQ+)>
<!ELEMENT BUGTRAQ (ID, URL)>
<!ELEMENT ID (#PCDATA)>
<!ELEMENT URL (#PCDATA)>
<!ELEMENT PATCHABLE (#PCDATA)>
<!ELEMENT SOFTWARE_LIST (SOFTWARE+)>
<!ELEMENT SOFTWARE (PRODUCT, VENDOR)>
<!ELEMENT PRODUCT (#PCDATA)>
<!ELEMENT VENDOR (#PCDATA)>
<!ELEMENT VENDOR_REFERENCE_LIST (VENDOR_REFERENCE+)>
<!ELEMENT VENDOR_REFERENCE (ID, URL)>
<!ELEMENT CVE_LIST (CVE+)>
<!ELEMENT CVE (ID, URL)>
<!-- ID, URL already defined -->
<!ELEMENT DIAGNOSIS (#PCDATA)>
<!ELEMENT DIAGNOSIS_COMMENT (#PCDATA)>
<!ELEMENT CONSEQUENCE (#PCDATA)>
<!ELEMENT CONSEQUENCE_COMMENT (#PCDATA)>
<!ELEMENT SOLUTION (#PCDATA)>
<!ELEMENT SOLUTION_COMMENT (#PCDATA)>
<!ELEMENT COMPLIANCE_LIST (COMPLIANCE+)>
<!ELEMENT COMPLIANCE (TYPE, SECTION, DESCRIPTION)>
<!ELEMENT TYPE (#PCDATA)>
<!ELEMENT SECTION (#PCDATA)>
<!ELEMENT DESCRIPTION (#PCDATA)>
<!ELEMENT CORRELATION (EXPLOITS?, MALWARE?)>
<!ELEMENT EXPLOITS (EXPLT_SRC+)>
<!ELEMENT EXPLT_SRC (SRC_NAME, EXPLT_LIST)>
<!ELEMENT SRC_NAME (#PCDATA)>
<!ELEMENT EXPLT_LIST (EXPLT+)>
<!ELEMENT EXPLT (REF, DESC, LINK?)>
<!ELEMENT REF (#PCDATA)>
<!ELEMENT DESC (#PCDATA)>
<!ELEMENT LINK (#PCDATA)>
<!ELEMENT MALWARE (MW_SRC+)>
<!ELEMENT MW_SRC (SRC_NAME, MW_LIST)>
<!ELEMENT MW_LIST (MW_INFO+)>
<!ELEMENT MW_INFO (MW_ID, MW_TYPE?, MW_PLATFORM?,
MW_ALIAS?, MW_RATING?, MW_LINK?)>
<!ELEMENT MW_ID (#PCDATA)>
<!ELEMENT MW_TYPE (#PCDATA)>
<!ELEMENT MW_PLATFORM (#PCDATA)>
<!ELEMENT MW_ALIAS (#PCDATA)>
<!ELEMENT MW_RATING (#PCDATA)>
<!ELEMENT MW_LINK (#PCDATA)>
<!ELEMENT CVSS (BASE?, TEMPORAL?, VECTOR_STRING?, ACCESS?,
    IMPACT?, AUTHENTICATION?, EXPLOITABILITY?,
    REMEDIATION_LEVEL?, REPORT_CONFIDENCE?)>
<!ELEMENT BASE (#PCDATA)>
<!ATTLIST BASE source CDATA #IMPLIED>
<!ELEMENT TEMPORAL (#PCDATA)>
<!ELEMENT VECTOR_STRING (#PCDATA)>
<!ELEMENT ACCESS (VECTOR?, COMPLEXITY?)>
<!ELEMENT VECTOR (#PCDATA)>
<!ELEMENT COMPLEXITY (#PCDATA)>
<!ELEMENT IMPACT (
    CONFIDENTIALITY?,
    INTEGRITY?,
    AVAILABILITY?
)>
<!ELEMENT CONFIDENTIALITY (#PCDATA)>
<!ELEMENT INTEGRITY (#PCDATA)>
<!ELEMENT AVAILABILITY (#PCDATA)>
<!ELEMENT AUTHENTICATION (#PCDATA)>
<!ELEMENT EXPLOITABILITY (#PCDATA)>
<!ELEMENT REMEDIATION_LEVEL (#PCDATA)>
<!ELEMENT REPORT_CONFIDENCE (#PCDATA)>
<!ELEMENT CVSS_V3 (BASE?, TEMPORAL?, VECTOR_STRING?, ATTACK?,
IMPACT?, PRIVILEGES_REQUIRED?, USER_INTERACTION?, SCOPE?,
EXPLOIT_CODE_MATURITY?, REMEDIATION_LEVEL?,
REPORT_CONFIDENCE?)>
<!ELEMENT ATTACK (
    VECTOR?, COMPLEXITY?
)>
<!ELEMENT PRIVILEGES_REQUIRED (#PCDATA)>
<!ELEMENT USER_INTERACTION (#PCDATA)>
<!ELEMENT SCOPE (#PCDATA)>
<!ELEMENT EXPLOIT_CODE_MATURITY (#PCDATA)>
<!ELEMENT PCI_FLAG (#PCDATA)>
<!ELEMENT AUTOMATIC_PCI_FAIL (#PCDATA)>
<!ELEMENT PCI_REASONS (PCI_REASON+)>
<!ELEMENT PCI_REASON (#PCDATA)>
<!ELEMENT THREAT_INTELLIGENCE (THREAT_INTEL+)>
<!ELEMENT THREAT_INTEL (#PCDATA)>
<!ATTLIST THREAT_INTEL
    id CDATA #REQUIRED>
<!ELEMENT SUPPORTED_MODULES (#PCDATA)>
<!ELEMENT DISCOVERY (REMOTE, AUTH_TYPE_LIST?, ADDITIONAL_INFO?)>
<!ELEMENT REMOTE (#PCDATA)>
<!ELEMENT AUTH_TYPE_LIST (AUTH_TYPE+)>
<!ELEMENT AUTH_TYPE (#PCDATA)>
<!ELEMENT ADDITIONAL_INFO (#PCDATA)>
<!ELEMENT IS_DISABLED (#PCDATA)>
<!ELEMENT CHANGE_LOG_LIST (CHANGE_LOG_INFO+)>
<!ELEMENT CHANGE_LOG_INFO (CHANGE_DATE, COMMENTS)>
<!ELEMENT CHANGE_DATE (#PCDATA)>
<!ELEMENT COMMENTS (#PCDATA)>
<!ELEMENT ID_SET ((ID|ID_RANGE)+)>
<!-- ID already defined -->
<!ELEMENT ID_RANGE (#PCDATA)>
<!ELEMENT WARNING (CODE?, TEXT, URL?)>
<!ELEMENT CODE (#PCDATA)>
<!ELEMENT TEXT (#PCDATA)>
<!-- URL already defined -->
<!-- EOF -->
"""

"""
XML DTD To Pydantic Data Model Converter
"""

from typing import IO, Optional
from xml.etree import ElementTree



def xml_to_dict(element):
    result = {}

    if (element.text or '').strip():
        result['__cdata'] = element.text.strip()

    result.update({f'_{key}': value for key, value in element.attrib.items()})
    
    for nested_tag in element:
        tag = nested_tag.tag
        nested_element = xml_to_dict(nested_tag)

        if tag in result:
            if not isinstance(result[tag], list):
                result[tag] = [result.pop(tag)]
            result[tag].append(nested_element)
        else:
            result[tag] = nested_element
    
    return result


def iter_parse_xml(fp: IO, element_hook: Optional[str] = None):
    xml_iter = ElementTree.iterparse(fp, events=['end'])
    full_document, last_element_seen = None, None

    for _, element in xml_iter:
        last_element_seen = element
        yield full_document, xml_to_dict(element)
    
    full_document = xml_to_dict(last_element_seen)

    yield full_document, None


def load_xml(fp: IO, element_hook: Optional[str] = None):
    if element_hook:
        return iter_parse_xml(fp)
    else:
        return xml_to_dict(ElementTree.parse(fp).getroot())


from pydantic import BaseModel, Field, validator


class Xml(BaseModel):
    class Config:
        validate_all = True
        validate_assignment = True
        allow_population_by_field_name = True
        extra = 'allow'
    
    def __str__(self) -> str:
        return self.json()
    
    def __repr__(self) -> str:
        return str(self)
    
    def __format__(self, format_spect) -> str:
        return str(self)
    
    def __hash__(self) -> int:
        return hash(self.json())
    
    def attributes(self):
        # * Use __dict__ rather than __fields__ to support extra = 'allow'
        return [
            getattr(self, attr.name)
            for attr in self.__dict__.values() if attr.name.startswith('_')
            and not attr.name.startswith('__')
        ]
    
    def dict(self, *args, **kwargs):
        by_alias = kwargs.pop('by_alias', True)
        return BaseModel.dict(self, *args, by_alias=by_alias, **kwargs)

    def json(self, *args, **kwargs):
        by_alias = kwargs.pop('by_alias', True)
        return BaseModel.json(self, *args, by_alias=by_alias, **kwargs)
    
    cdata: Optional[str] = Field(alias='__cdata')


class EMPTY(Xml):  # https://www.w3schools.com/xml/xml_dtd_elements.asp
    ...











# pprint.pprint(load_xml(open('xml.xml')))

elements = re.compile(r'<!(?!--)[\s\S\n]*?>')

dtd = elements.findall(__doc__)

print(__doc__)
# pprint.pprint(dtd)



elements = [' '.join(i.split()) for i in dtd if 'ELEMENT' in i]
attributes = [i for i in dtd if 'ATTLIST' in i]

elements = [i.split(maxsplit=1)[1].replace('>', '') for i in elements]
elements = [tuple(i.split(maxsplit=1)) for i in elements]
elements = [(i[0], i[1].strip()) for i in elements]

pprint.pprint(elements)
pprint.pprint(attributes)


"""
(A | B):
    Union[A, B]
(A | (B | C)):
    Union[A, Union[B, C]]
A+:
    List[A]
A*:
    List[A]
A?:
    Optional[A]
"""



class Token(list): ...
class TokenUnion(Token): ...
class TokenList(Token): ...
class TokenOptional(Token): ...
class TokenGroup(Token): ...


name, element = elements[0]


print('\n\n\n', name, ':', element, '\n')

"""
((#PCDATA | TO | FROM | HEADER | MESSAGE)*):
    List[Union[Xml, TO, FROM, HEADER, MESSAGE]]


"""

# TASK: Convert this:
tokens = ['(', '|', '(', '#PCDATA', '']
# Into this:
code = [
    'PUSH group()',
    'PUSH list()',
    'PUSH union()',
    'PUSH XML',
    'POP',
    'PUSH TO',
    'POP',
    'PUSH FROM',
    'POP',
    'PUSH HEADER',
    'POP',
    'PUSH MESSAGE',
    'POP',
    'POP',
    'POP'
]

# ! Popping a group checks if it only contains one element and returns that

# ( TO, FROM?, (HEADING+, BODY*), (PS | PPS) )

from pyparsing import *

Symbol = Word(alphas, bodyChars=alphanums + '_')
wh = Optional(White() | LineEnd()).suppress()
List = Literal('+') | Literal('*')
Option = Literal('?')
Modifier = List | Option

FrameForward = Forward()

Frame = Group(
    Literal('(').suppress() + wh +
    OneOrMore(
        (FrameForward | (Group(OneOrMore(Symbol + wh + Literal('|') + wh) + Symbol)) | Symbol) + wh +
        Optional(Modifier) + wh +
        Optional(Literal(',')).suppress() + wh
    ) +
    Literal(')').suppress() + wh
)

FrameForward << Frame

print(Frame.parseString(element))


print()

for name, element in elements:
    print(Frame.parseString(element))
