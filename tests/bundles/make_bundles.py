true, false, null = True, False, None

weaknesses = [
  {
    "common_consequences": [
      "Other"
    ],
    "created": "2006-07-19T00:00:00.000Z",
    "created_by_ref": "identity--d91de5c9-2d85-5cc9-97c0-c5ec8deb1a4b",
    "description": "Duplicate keys in associative lists can lead to non-unique keys being mistaken for an error.\nA duplicate key entry -- if the alist is designed properly -- could be used as a constant time replace function. However, duplicate key entries could be inserted by mistake. Because of this ambiguity, duplicate key entries in an association list are not recommended and should not be allowed.",
    "extensions": {
      "extension-definition--31725edc-7d81-5db7-908a-9134f322284a": {
        "extension_type": "new-sdo"
      }
    },
    "external_references": [
      {
        "source_name": "cwe",
        "url": "http://cwe.mitre.org/data/definitions/462.html",
        "external_id": "CWE-462"
      },
      {
        "source_name": "Secure Software, Inc.",
        "description": "The CLASP Application Security Process",
        "url": "https://cwe.mitre.org/documents/sources/TheCLASPApplicationSecurityProcess.pdf",
        "external_id": "REF-18"
      },
      {
        "source_name": "CLASP",
        "description": "Duplicate key in associative list (alist)"
      },
      {
        "source_name": "CERT C Secure Coding",
        "description": "Beware of multiple environment variables with the same effective name",
        "external_id": "ENV02-C"
      }
    ],
    "id": "weakness--020b8df8-7e0d-5672-80dc-1918c70c5725",
    "likelihood_of_exploit": [
      "Low"
    ],
    "modes_of_introduction": [
      "Architecture and Design",
      "Implementation"
    ],
    "modified": "2020-02-24T00:00:00.000Z",
    "name": "Duplicate Key in Associative List (Alist)",
    "object_marking_refs": [
      "marking-definition--94868c89-83c2-464b-929b-a1a8aa3c8487",
      "marking-definition--d91de5c9-2d85-5cc9-97c0-c5ec8deb1a4b"
    ],
    "spec_version": "2.1",
    "type": "weakness"
  },
  {
    "common_consequences": [
      "Other"
    ],
    "created": "2006-07-19T00:00:00.000Z",
    "created_by_ref": "identity--d91de5c9-2d85-5cc9-97c0-c5ec8deb1a4b",
    "description": "Duplicate keys in associative lists can lead to non-unique keys being mistaken for an error.\nA duplicate key entry -- if the alist is designed properly -- could be used as a constant time replace function. However, duplicate key entries could be inserted by mistake. Because of this ambiguity, duplicate key entries in an association list are not recommended and should not be allowed.",
    "extensions": {
      "extension-definition--31725edc-7d81-5db7-908a-9134f322284a": {
        "extension_type": "new-sdo"
      }
    },
    "external_references": [
      {
        "source_name": "cwe",
        "url": "http://cwe.mitre.org/data/definitions/462.html",
        "external_id": "CWE-462"
      },
      {
        "source_name": "Secure Software, Inc.",
        "description": "The CLASP Application Security Process",
        "url": "https://cwe.mitre.org/documents/sources/TheCLASPApplicationSecurityProcess.pdf",
        "external_id": "REF-18"
      },
      {
        "source_name": "CLASP",
        "description": "Duplicate key in associative list (alist)"
      },
      {
        "source_name": "CERT C Secure Coding",
        "description": "Beware of multiple environment variables with the same effective name",
        "external_id": "ENV02-C"
      }
    ],
    "id": "weakness--020b8df8-7e0d-5672-80dc-1918c70c5725",
    "likelihood_of_exploit": [
      "Low"
    ],
    "modes_of_introduction": [
      "Implementation"
    ],
    "modified": "2023-04-27T00:00:00.000Z",
    "name": "Duplicate Key in Associative List (Alist)",
    "object_marking_refs": [
      "marking-definition--94868c89-83c2-464b-929b-a1a8aa3c8487",
      "marking-definition--d91de5c9-2d85-5cc9-97c0-c5ec8deb1a4b"
    ],
    "spec_version": "2.1",
    "type": "weakness"
  },
  {
    "common_consequences": [
      "Other"
    ],
    "created": "2006-07-19T00:00:00.000Z",
    "created_by_ref": "identity--d91de5c9-2d85-5cc9-97c0-c5ec8deb1a4b",
    "description": "Duplicate keys in associative lists can lead to non-unique keys being mistaken for an error.\nA duplicate key entry -- if the alist is designed properly -- could be used as a constant time replace function. However, duplicate key entries could be inserted by mistake. Because of this ambiguity, duplicate key entries in an association list are not recommended and should not be allowed.",
    "extensions": {
      "extension-definition--31725edc-7d81-5db7-908a-9134f322284a": {
        "extension_type": "new-sdo"
      }
    },
    "external_references": [
      {
        "source_name": "cwe",
        "url": "http://cwe.mitre.org/data/definitions/462.html",
        "external_id": "CWE-462"
      },
      {
        "source_name": "Secure Software, Inc.",
        "description": "The CLASP Application Security Process",
        "url": "https://cwe.mitre.org/documents/sources/TheCLASPApplicationSecurityProcess.pdf",
        "external_id": "REF-18"
      },
      {
        "source_name": "CLASP",
        "description": "Duplicate key in associative list (alist)"
      },
      {
        "source_name": "CERT C Secure Coding",
        "description": "Beware of multiple environment variables with the same effective name",
        "external_id": "ENV02-C"
      }
    ],
    "id": "weakness--020b8df8-7e0d-5672-80dc-1918c70c5725",
    "likelihood_of_exploit": [
      "Low"
    ],
    "modes_of_introduction": [
      "Implementation"
    ],
    "modified": "2023-06-29T00:00:00.000Z",
    "name": "Duplicate Key in Associative List (Alist)",
    "object_marking_refs": [
      "marking-definition--94868c89-83c2-464b-929b-a1a8aa3c8487",
      "marking-definition--d91de5c9-2d85-5cc9-97c0-c5ec8deb1a4b"
    ],
    "spec_version": "2.1",
    "type": "weakness"
  },
  {
    "common_consequences": [
      "Confidentiality"
    ],
    "created": "2006-07-19T00:00:00.000Z",
    "created_by_ref": "identity--d91de5c9-2d85-5cc9-97c0-c5ec8deb1a4b",
    "description": "A backup file is stored in a directory or archive that is made accessible to unauthorized actors.\nOften, older backup files are renamed with an extension such as .~bk to distinguish them from production files. The source code for old files that have been renamed in this manner and left in the webroot can often be retrieved. This renaming may have been performed automatically by the web server, or manually by the administrator.",
    "extensions": {
      "extension-definition--31725edc-7d81-5db7-908a-9134f322284a": {
        "extension_type": "new-sdo"
      }
    },
    "external_references": [
      {
        "source_name": "cwe",
        "url": "http://cwe.mitre.org/data/definitions/530.html",
        "external_id": "CWE-530"
      }
    ],
    "id": "weakness--02ccafe3-fb87-5b5e-8639-117d6e87a2c7",
    "modes_of_introduction": [
      "Operation"
    ],
    "modified": "2020-02-24T00:00:00.000Z",
    "name": "Exposure of Backup File to an Unauthorized Control Sphere",
    "object_marking_refs": [
      "marking-definition--94868c89-83c2-464b-929b-a1a8aa3c8487",
      "marking-definition--d91de5c9-2d85-5cc9-97c0-c5ec8deb1a4b"
    ],
    "spec_version": "2.1",
    "type": "weakness"
  },
  {
    "common_consequences": [
      "Confidentiality"
    ],
    "created": "2006-07-19T00:00:00.000Z",
    "created_by_ref": "identity--d91de5c9-2d85-5cc9-97c0-c5ec8deb1a4b",
    "description": "A backup file is stored in a directory or archive that is made accessible to unauthorized actors.\nOften, older backup files are renamed with an extension such as .~bk to distinguish them from production files. The source code for old files that have been renamed in this manner and left in the webroot can often be retrieved. This renaming may have been performed automatically by the web server, or manually by the administrator.",
    "detection_methods": [
      "Automated Static Analysis"
    ],
    "extensions": {
      "extension-definition--31725edc-7d81-5db7-908a-9134f322284a": {
        "extension_type": "new-sdo"
      }
    },
    "external_references": [
      {
        "source_name": "cwe",
        "url": "http://cwe.mitre.org/data/definitions/530.html",
        "external_id": "CWE-530"
      }
    ],
    "id": "weakness--02ccafe3-fb87-5b5e-8639-117d6e87a2c7",
    "modes_of_introduction": [
      "Operation"
    ],
    "modified": "2023-04-27T00:00:00.000Z",
    "name": "Exposure of Backup File to an Unauthorized Control Sphere",
    "object_marking_refs": [
      "marking-definition--94868c89-83c2-464b-929b-a1a8aa3c8487",
      "marking-definition--d91de5c9-2d85-5cc9-97c0-c5ec8deb1a4b"
    ],
    "spec_version": "2.1",
    "type": "weakness"
  },
  {
    "common_consequences": [
      "Confidentiality"
    ],
    "created": "2006-07-19T00:00:00.000Z",
    "created_by_ref": "identity--d91de5c9-2d85-5cc9-97c0-c5ec8deb1a4b",
    "description": "A backup file is stored in a directory or archive that is made accessible to unauthorized actors.\nOften, older backup files are renamed with an extension such as .~bk to distinguish them from production files. The source code for old files that have been renamed in this manner and left in the webroot can often be retrieved. This renaming may have been performed automatically by the web server, or manually by the administrator.",
    "detection_methods": [
      "Automated Static Analysis"
    ],
    "extensions": {
      "extension-definition--31725edc-7d81-5db7-908a-9134f322284a": {
        "extension_type": "new-sdo"
      }
    },
    "external_references": [
      {
        "source_name": "cwe",
        "url": "http://cwe.mitre.org/data/definitions/530.html",
        "external_id": "CWE-530"
      }
    ],
    "id": "weakness--02ccafe3-fb87-5b5e-8639-117d6e87a2c7",
    "modes_of_introduction": [
      "Operation"
    ],
    "modified": "2023-06-29T00:00:00.000Z",
    "name": "Exposure of Backup File to an Unauthorized Control Sphere",
    "object_marking_refs": [
      "marking-definition--94868c89-83c2-464b-929b-a1a8aa3c8487",
      "marking-definition--d91de5c9-2d85-5cc9-97c0-c5ec8deb1a4b"
    ],
    "spec_version": "2.1",
    "type": "weakness"
  },
  {
    "common_consequences": [
      "Other"
    ],
    "created": "2006-12-15T00:00:00.000Z",
    "created_by_ref": "identity--d91de5c9-2d85-5cc9-97c0-c5ec8deb1a4b",
    "description": "The product uses the wrong operator when comparing a string, such as using \"==\" when the .equals() method should be used instead.\nIn Java, using == or != to compare two strings for equality actually compares two objects for equality rather than their string values for equality. Chances are good that the two references will never be equal. While this weakness often only affects program correctness, if the equality is used for a security decision, the unintended comparison result could be leveraged to affect program security.",
    "extensions": {
      "extension-definition--31725edc-7d81-5db7-908a-9134f322284a": {
        "extension_type": "new-sdo"
      }
    },
    "external_references": [
      {
        "source_name": "cwe",
        "url": "http://cwe.mitre.org/data/definitions/597.html",
        "external_id": "CWE-597"
      },
      {
        "source_name": "Mark Dowd, John McDonald, Justin Schuh",
        "description": "The Art of Software Security Assessment",
        "external_id": "REF-62"
      },
      {
        "source_name": "The CERT Oracle Secure Coding Standard for Java (2011)",
        "description": "Do not use the equality operators when comparing values of boxed primitives",
        "external_id": "EXP03-J"
      },
      {
        "source_name": "The CERT Oracle Secure Coding Standard for Java (2011)",
        "description": "Do not use the equality operators when comparing values of boxed primitives",
        "external_id": "EXP03-J"
      },
      {
        "source_name": "SEI CERT Perl Coding Standard",
        "description": "Use the correct operator type for comparing values",
        "external_id": "EXP35-PL"
      },
      {
        "source_name": "Software Fault Patterns",
        "description": "Glitch in computation",
        "external_id": "SFP1"
      }
    ],
    "id": "weakness--044d9bdf-3610-5bc2-8c72-bf5b86f91dd2",
    "modes_of_introduction": [
      "Implementation"
    ],
    "modified": "2021-03-15T00:00:00.000Z",
    "name": "Use of Wrong Operator in String Comparison",
    "object_marking_refs": [
      "marking-definition--94868c89-83c2-464b-929b-a1a8aa3c8487",
      "marking-definition--d91de5c9-2d85-5cc9-97c0-c5ec8deb1a4b"
    ],
    "spec_version": "2.1",
    "type": "weakness"
  },
  {
    "common_consequences": [
      "Other"
    ],
    "created": "2006-12-15T00:00:00.000Z",
    "created_by_ref": "identity--d91de5c9-2d85-5cc9-97c0-c5ec8deb1a4b",
    "description": "The product uses the wrong operator when comparing a string, such as using \"==\" when the .equals() method should be used instead.\nIn Java, using == or != to compare two strings for equality actually compares two objects for equality rather than their string values for equality. Chances are good that the two references will never be equal. While this weakness often only affects program correctness, if the equality is used for a security decision, the unintended comparison result could be leveraged to affect program security.",
    "detection_methods": [
      "Automated Static Analysis"
    ],
    "extensions": {
      "extension-definition--31725edc-7d81-5db7-908a-9134f322284a": {
        "extension_type": "new-sdo"
      }
    },
    "external_references": [
      {
        "source_name": "cwe",
        "url": "http://cwe.mitre.org/data/definitions/597.html",
        "external_id": "CWE-597"
      },
      {
        "source_name": "Mark Dowd, John McDonald, Justin Schuh",
        "description": "The Art of Software Security Assessment",
        "external_id": "REF-62"
      },
      {
        "source_name": "The CERT Oracle Secure Coding Standard for Java (2011)",
        "description": "Do not use the equality operators when comparing values of boxed primitives",
        "external_id": "EXP03-J"
      },
      {
        "source_name": "The CERT Oracle Secure Coding Standard for Java (2011)",
        "description": "Do not use the equality operators when comparing values of boxed primitives",
        "external_id": "EXP03-J"
      },
      {
        "source_name": "SEI CERT Perl Coding Standard",
        "description": "Use the correct operator type for comparing values",
        "external_id": "EXP35-PL"
      },
      {
        "source_name": "Software Fault Patterns",
        "description": "Glitch in computation",
        "external_id": "SFP1"
      }
    ],
    "id": "weakness--044d9bdf-3610-5bc2-8c72-bf5b86f91dd2",
    "modes_of_introduction": [
      "Implementation"
    ],
    "modified": "2023-04-27T00:00:00.000Z",
    "name": "Use of Wrong Operator in String Comparison",
    "object_marking_refs": [
      "marking-definition--94868c89-83c2-464b-929b-a1a8aa3c8487",
      "marking-definition--d91de5c9-2d85-5cc9-97c0-c5ec8deb1a4b"
    ],
    "spec_version": "2.1",
    "type": "weakness"
  },
  {
    "common_consequences": [
      "Other"
    ],
    "created": "2006-12-15T00:00:00.000Z",
    "created_by_ref": "identity--d91de5c9-2d85-5cc9-97c0-c5ec8deb1a4b",
    "description": "The product uses the wrong operator when comparing a string, such as using \"==\" when the .equals() method should be used instead.\nIn Java, using == or != to compare two strings for equality actually compares two objects for equality rather than their string values for equality. Chances are good that the two references will never be equal. While this weakness often only affects program correctness, if the equality is used for a security decision, the unintended comparison result could be leveraged to affect program security.",
    "detection_methods": [
      "Automated Static Analysis"
    ],
    "extensions": {
      "extension-definition--31725edc-7d81-5db7-908a-9134f322284a": {
        "extension_type": "new-sdo"
      }
    },
    "external_references": [
      {
        "source_name": "cwe",
        "url": "http://cwe.mitre.org/data/definitions/597.html",
        "external_id": "CWE-597"
      },
      {
        "source_name": "Mark Dowd, John McDonald, Justin Schuh",
        "description": "The Art of Software Security Assessment",
        "external_id": "REF-62"
      },
      {
        "source_name": "The CERT Oracle Secure Coding Standard for Java (2011)",
        "description": "Do not use the equality operators when comparing values of boxed primitives",
        "external_id": "EXP03-J"
      },
      {
        "source_name": "The CERT Oracle Secure Coding Standard for Java (2011)",
        "description": "Do not use the equality operators when comparing values of boxed primitives",
        "external_id": "EXP03-J"
      },
      {
        "source_name": "SEI CERT Perl Coding Standard",
        "description": "Use the correct operator type for comparing values",
        "external_id": "EXP35-PL"
      },
      {
        "source_name": "Software Fault Patterns",
        "description": "Glitch in computation",
        "external_id": "SFP1"
      }
    ],
    "id": "weakness--044d9bdf-3610-5bc2-8c72-bf5b86f91dd2",
    "modes_of_introduction": [
      "Implementation"
    ],
    "modified": "2023-06-29T00:00:00.000Z",
    "name": "Use of Wrong Operator in String Comparison",
    "object_marking_refs": [
      "marking-definition--94868c89-83c2-464b-929b-a1a8aa3c8487",
      "marking-definition--d91de5c9-2d85-5cc9-97c0-c5ec8deb1a4b"
    ],
    "spec_version": "2.1",
    "type": "weakness"
  },
  {
    "common_consequences": [
      "Integrity"
    ],
    "created": "2007-05-07T00:00:00.000Z",
    "created_by_ref": "identity--d91de5c9-2d85-5cc9-97c0-c5ec8deb1a4b",
    "description": "The product does not properly handle null bytes or NUL characters when passing data between different representations or components.\n<html:p>A null byte (NUL character) can have different meanings across representations or languages. For example, it is a string terminator in standard C libraries, but Perl and PHP strings do not treat it as a terminator. When two representations are crossed - such as when Perl or PHP invokes underlying C functionality - this can produce an interaction error with unexpected results. Similar issues have been reported for ASP. Other interpreters written in C might also be affected.</html:p>\n            <html:p>The poison null byte is frequently useful in path traversal attacks by terminating hard-coded extensions that are added to a filename. It can play a role in regular expression processing in PHP.</html:p>\n         ",
    "extensions": {
      "extension-definition--31725edc-7d81-5db7-908a-9134f322284a": {
        "extension_type": "new-sdo"
      }
    },
    "external_references": [
      {
        "source_name": "cwe",
        "url": "http://cwe.mitre.org/data/definitions/626.html",
        "external_id": "CWE-626"
      },
      {
        "source_name": "Rain Forest Puppy",
        "description": "Poison NULL byte",
        "url": "http://insecure.org/news/P55-07.txt",
        "external_id": "REF-514"
      },
      {
        "source_name": "Brett Moore",
        "description": "0x00 vs ASP file upload scripts",
        "url": "http://www.security-assessment.com/Whitepapers/0x00_vs_ASP_File_Uploads.pdf",
        "external_id": "REF-515"
      },
      {
        "source_name": "ShAnKaR",
        "description": "ShAnKaR: multiple PHP application poison NULL byte vulnerability",
        "url": "http://seclists.org/fulldisclosure/2006/Sep/0185.html",
        "external_id": "REF-516"
      }
    ],
    "id": "weakness--054fa434-776d-5b30-9566-809507993dd0",
    "modes_of_introduction": [
      "Implementation"
    ],
    "modified": "2020-06-25T00:00:00.000Z",
    "name": "Null Byte Interaction Error (Poison Null Byte)",
    "object_marking_refs": [
      "marking-definition--94868c89-83c2-464b-929b-a1a8aa3c8487",
      "marking-definition--d91de5c9-2d85-5cc9-97c0-c5ec8deb1a4b"
    ],
    "spec_version": "2.1",
    "type": "weakness"
  },
  {
    "common_consequences": [
      "Integrity"
    ],
    "created": "2007-05-07T00:00:00.000Z",
    "created_by_ref": "identity--d91de5c9-2d85-5cc9-97c0-c5ec8deb1a4b",
    "description": "The product does not properly handle null bytes or NUL characters when passing data between different representations or components.\n<html:p>A null byte (NUL character) can have different meanings across representations or languages. For example, it is a string terminator in standard C libraries, but Perl and PHP strings do not treat it as a terminator. When two representations are crossed - such as when Perl or PHP invokes underlying C functionality - this can produce an interaction error with unexpected results. Similar issues have been reported for ASP. Other interpreters written in C might also be affected.</html:p>\n            <html:p>The poison null byte is frequently useful in path traversal attacks by terminating hard-coded extensions that are added to a filename. It can play a role in regular expression processing in PHP.</html:p>\n         ",
    "extensions": {
      "extension-definition--31725edc-7d81-5db7-908a-9134f322284a": {
        "extension_type": "new-sdo"
      }
    },
    "external_references": [
      {
        "source_name": "cwe",
        "url": "http://cwe.mitre.org/data/definitions/626.html",
        "external_id": "CWE-626"
      },
      {
        "source_name": "Rain Forest Puppy",
        "description": "Poison NULL byte",
        "url": "https://insecure.org/news/P55-07.txt",
        "external_id": "REF-514"
      },
      {
        "source_name": "Brett Moore",
        "description": "0x00 vs ASP file upload scripts",
        "url": "http://www.security-assessment.com/Whitepapers/0x00_vs_ASP_File_Uploads.pdf",
        "external_id": "REF-515"
      },
      {
        "source_name": "ShAnKaR",
        "description": "ShAnKaR: multiple PHP application poison NULL byte vulnerability",
        "url": "https://seclists.org/fulldisclosure/2006/Sep/185",
        "external_id": "REF-516"
      }
    ],
    "id": "weakness--054fa434-776d-5b30-9566-809507993dd0",
    "modes_of_introduction": [
      "Implementation"
    ],
    "modified": "2023-04-27T00:00:00.000Z",
    "name": "Null Byte Interaction Error (Poison Null Byte)",
    "object_marking_refs": [
      "marking-definition--94868c89-83c2-464b-929b-a1a8aa3c8487",
      "marking-definition--d91de5c9-2d85-5cc9-97c0-c5ec8deb1a4b"
    ],
    "spec_version": "2.1",
    "type": "weakness"
  },
  {
    "common_consequences": [
      "Integrity"
    ],
    "created": "2007-05-07T00:00:00.000Z",
    "created_by_ref": "identity--d91de5c9-2d85-5cc9-97c0-c5ec8deb1a4b",
    "description": "The product does not properly handle null bytes or NUL characters when passing data between different representations or components.\n<html:p>A null byte (NUL character) can have different meanings across representations or languages. For example, it is a string terminator in standard C libraries, but Perl and PHP strings do not treat it as a terminator. When two representations are crossed - such as when Perl or PHP invokes underlying C functionality - this can produce an interaction error with unexpected results. Similar issues have been reported for ASP. Other interpreters written in C might also be affected.</html:p>\n            <html:p>The poison null byte is frequently useful in path traversal attacks by terminating hard-coded extensions that are added to a filename. It can play a role in regular expression processing in PHP.</html:p>\n         ",
    "extensions": {
      "extension-definition--31725edc-7d81-5db7-908a-9134f322284a": {
        "extension_type": "new-sdo"
      }
    },
    "external_references": [
      {
        "source_name": "cwe",
        "url": "http://cwe.mitre.org/data/definitions/626.html",
        "external_id": "CWE-626"
      },
      {
        "source_name": "Rain Forest Puppy",
        "description": "Poison NULL byte",
        "url": "https://insecure.org/news/P55-07.txt",
        "external_id": "REF-514"
      },
      {
        "source_name": "Brett Moore",
        "description": "0x00 vs ASP file upload scripts",
        "url": "http://www.security-assessment.com/Whitepapers/0x00_vs_ASP_File_Uploads.pdf",
        "external_id": "REF-515"
      },
      {
        "source_name": "ShAnKaR",
        "description": "ShAnKaR: multiple PHP application poison NULL byte vulnerability",
        "url": "https://seclists.org/fulldisclosure/2006/Sep/185",
        "external_id": "REF-516"
      }
    ],
    "id": "weakness--054fa434-776d-5b30-9566-809507993dd0",
    "modes_of_introduction": [
      "Implementation"
    ],
    "modified": "2023-06-29T00:00:00.000Z",
    "name": "Null Byte Interaction Error (Poison Null Byte)",
    "object_marking_refs": [
      "marking-definition--94868c89-83c2-464b-929b-a1a8aa3c8487",
      "marking-definition--d91de5c9-2d85-5cc9-97c0-c5ec8deb1a4b"
    ],
    "spec_version": "2.1",
    "type": "weakness"
  },
  {
    "common_consequences": [
      "Integrity",
      "Confidentiality"
    ],
    "created": "2006-07-19T00:00:00.000Z",
    "created_by_ref": "identity--d91de5c9-2d85-5cc9-97c0-c5ec8deb1a4b",
    "description": "An object contains a public static field that is not marked final, which might allow it to be modified in unexpected ways.\nPublic static variables can be read without an accessor and changed without a mutator by any classes in the application.",
    "extensions": {
      "extension-definition--31725edc-7d81-5db7-908a-9134f322284a": {
        "extension_type": "new-sdo"
      }
    },
    "external_references": [
      {
        "source_name": "cwe",
        "url": "http://cwe.mitre.org/data/definitions/500.html",
        "external_id": "CWE-500"
      },
      {
        "source_name": "Secure Software, Inc.",
        "description": "The CLASP Application Security Process",
        "url": "https://cwe.mitre.org/documents/sources/TheCLASPApplicationSecurityProcess.pdf",
        "external_id": "REF-18"
      },
      {
        "source_name": "CLASP",
        "description": "Overflow of static internal buffer"
      },
      {
        "source_name": "The CERT Oracle Secure Coding Standard for Java (2011)",
        "description": "Do not use public static nonfinal variables",
        "external_id": "OBJ10-J"
      },
      {
        "source_name": "Software Fault Patterns",
        "description": "Unexpected access points",
        "external_id": "SFP28"
      }
    ],
    "id": "weakness--0e3285cb-3cba-5d16-8f2a-9449a6242793",
    "likelihood_of_exploit": [
      "High"
    ],
    "modes_of_introduction": [
      "Implementation"
    ],
    "modified": "2020-02-24T00:00:00.000Z",
    "name": "Public Static Field Not Marked Final",
    "object_marking_refs": [
      "marking-definition--94868c89-83c2-464b-929b-a1a8aa3c8487",
      "marking-definition--d91de5c9-2d85-5cc9-97c0-c5ec8deb1a4b"
    ],
    "spec_version": "2.1",
    "type": "weakness"
  },
  {
    "common_consequences": [
      "Integrity",
      "Confidentiality"
    ],
    "created": "2006-07-19T00:00:00.000Z",
    "created_by_ref": "identity--d91de5c9-2d85-5cc9-97c0-c5ec8deb1a4b",
    "description": "An object contains a public static field that is not marked final, which might allow it to be modified in unexpected ways.\nPublic static variables can be read without an accessor and changed without a mutator by any classes in the application.",
    "detection_methods": [
      "Automated Static Analysis"
    ],
    "extensions": {
      "extension-definition--31725edc-7d81-5db7-908a-9134f322284a": {
        "extension_type": "new-sdo"
      }
    },
    "external_references": [
      {
        "source_name": "cwe",
        "url": "http://cwe.mitre.org/data/definitions/500.html",
        "external_id": "CWE-500"
      },
      {
        "source_name": "Secure Software, Inc.",
        "description": "The CLASP Application Security Process",
        "url": "https://cwe.mitre.org/documents/sources/TheCLASPApplicationSecurityProcess.pdf",
        "external_id": "REF-18"
      },
      {
        "source_name": "CLASP",
        "description": "Overflow of static internal buffer"
      },
      {
        "source_name": "The CERT Oracle Secure Coding Standard for Java (2011)",
        "description": "Do not use public static nonfinal variables",
        "external_id": "OBJ10-J"
      },
      {
        "source_name": "Software Fault Patterns",
        "description": "Unexpected access points",
        "external_id": "SFP28"
      }
    ],
    "id": "weakness--0e3285cb-3cba-5d16-8f2a-9449a6242793",
    "likelihood_of_exploit": [
      "High"
    ],
    "modes_of_introduction": [
      "Implementation"
    ],
    "modified": "2023-04-27T00:00:00.000Z",
    "name": "Public Static Field Not Marked Final",
    "object_marking_refs": [
      "marking-definition--94868c89-83c2-464b-929b-a1a8aa3c8487",
      "marking-definition--d91de5c9-2d85-5cc9-97c0-c5ec8deb1a4b"
    ],
    "spec_version": "2.1",
    "type": "weakness"
  },
  {
    "common_consequences": [
      "Integrity",
      "Confidentiality"
    ],
    "created": "2006-07-19T00:00:00.000Z",
    "created_by_ref": "identity--d91de5c9-2d85-5cc9-97c0-c5ec8deb1a4b",
    "description": "An object contains a public static field that is not marked final, which might allow it to be modified in unexpected ways.\nPublic static variables can be read without an accessor and changed without a mutator by any classes in the application.",
    "detection_methods": [
      "Automated Static Analysis"
    ],
    "extensions": {
      "extension-definition--31725edc-7d81-5db7-908a-9134f322284a": {
        "extension_type": "new-sdo"
      }
    },
    "external_references": [
      {
        "source_name": "cwe",
        "url": "http://cwe.mitre.org/data/definitions/500.html",
        "external_id": "CWE-500"
      },
      {
        "source_name": "Secure Software, Inc.",
        "description": "The CLASP Application Security Process",
        "url": "https://cwe.mitre.org/documents/sources/TheCLASPApplicationSecurityProcess.pdf",
        "external_id": "REF-18"
      },
      {
        "source_name": "CLASP",
        "description": "Overflow of static internal buffer"
      },
      {
        "source_name": "The CERT Oracle Secure Coding Standard for Java (2011)",
        "description": "Do not use public static nonfinal variables",
        "external_id": "OBJ10-J"
      },
      {
        "source_name": "Software Fault Patterns",
        "description": "Unexpected access points",
        "external_id": "SFP28"
      }
    ],
    "id": "weakness--0e3285cb-3cba-5d16-8f2a-9449a6242793",
    "likelihood_of_exploit": [
      "High"
    ],
    "modes_of_introduction": [
      "Implementation"
    ],
    "modified": "2023-06-29T00:00:00.000Z",
    "name": "Public Static Field Not Marked Final",
    "object_marking_refs": [
      "marking-definition--94868c89-83c2-464b-929b-a1a8aa3c8487",
      "marking-definition--d91de5c9-2d85-5cc9-97c0-c5ec8deb1a4b"
    ],
    "spec_version": "2.1",
    "type": "weakness"
  }
]


attack_patterns = [
  {
    "created": "2020-01-14T17:18:32.126Z",
    "created_by_ref": "identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5",
    "description": "Adversaries may inject malicious code into process via Extra Window Memory (EWM) in order to evade process-based defenses as well as possibly elevate privileges. EWM injection is a method of executing arbitrary code in the address space of a separate live process. \n\nBefore creating a window, graphical Windows-based processes must prescribe to or register a windows class, which stipulate appearance and behavior (via windows procedures, which are functions that handle input/output of data).(Citation: Microsoft Window Classes) Registration of new windows classes can include a request for up to 40 bytes of EWM to be appended to the allocated memory of each instance of that class. This EWM is intended to store data specific to that window and has specific application programming interface (API) functions to set and get its value. (Citation: Microsoft GetWindowLong function) (Citation: Microsoft SetWindowLong function)\n\nAlthough small, the EWM is large enough to store a 32-bit pointer and is often used to point to a windows procedure. Malware may possibly utilize this memory location in part of an attack chain that includes writing code to shared sections of the process’s memory, placing a pointer to the code in EWM, then invoking execution by returning execution control to the address in the process’s EWM.\n\nExecution granted through EWM injection may allow access to both the target process's memory and possibly elevated privileges. Writing payloads to shared sections also avoids the use of highly monitored API calls such as <code>WriteProcessMemory</code> and <code>CreateRemoteThread</code>.(Citation: Endgame Process Injection July 2017) More sophisticated malware samples may also potentially bypass protection mechanisms such as data execution prevention (DEP) by triggering a combination of windows procedures and other system functions that will rewrite the malicious payload inside an executable portion of the target process.  (Citation: MalwareTech Power Loader Aug 2013) (Citation: WeLiveSecurity Gapz and Redyms Mar 2013)\n\nRunning code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via EWM injection may also evade detection from security products since the execution is masked under a legitimate process. ",
    "external_references": [
      {
        "source_name": "mitre-attack",
        "external_id": "T1055.011",
        "url": "https://attack.mitre.org/techniques/T1055/011"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633574.aspx",
        "description": "Microsoft. (n.d.). About Window Classes. Retrieved December 16, 2017.",
        "source_name": "Microsoft Window Classes"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633584.aspx",
        "description": "Microsoft. (n.d.). GetWindowLong function. Retrieved December 16, 2017.",
        "source_name": "Microsoft GetWindowLong function"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633591.aspx",
        "description": "Microsoft. (n.d.). SetWindowLong function. Retrieved December 16, 2017.",
        "source_name": "Microsoft SetWindowLong function"
      },
      {
        "url": "https://www.endgame.com/blog/technical-blog/ten-process-injection-techniques-technical-survey-common-and-trending-process",
        "description": "Hosseini, A. (2017, July 18). Ten Process Injection Techniques: A Technical Survey Of Common And Trending Process Injection Techniques. Retrieved December 7, 2017.",
        "source_name": "Endgame Process Injection July 2017"
      },
      {
        "url": "https://www.malwaretech.com/2013/08/powerloader-injection-something-truly.html",
        "description": "MalwareTech. (2013, August 13). PowerLoader Injection – Something truly amazing. Retrieved December 16, 2017.",
        "source_name": "MalwareTech Power Loader Aug 2013"
      },
      {
        "url": "https://www.welivesecurity.com/2013/03/19/gapz-and-redyms-droppers-based-on-power-loader-code/",
        "description": "Matrosov, A. (2013, March 19). Gapz and Redyms droppers based on Power Loader code. Retrieved December 16, 2017.",
        "source_name": "WeLiveSecurity Gapz and Redyms Mar 2013"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms644953.aspx",
        "description": "Microsoft. (n.d.). SendNotifyMessage function. Retrieved December 16, 2017.",
        "source_name": "Microsoft SendNotifyMessage function"
      }
    ],
    "id": "attack-pattern--0042a9f5-f053-4769-b3ef-9ad018dfa298",
    "kill_chain_phases": [
      {
        "kill_chain_name": "mitre-attack",
        "phase_name": "defense-evasion"
      },
      {
        "kill_chain_name": "mitre-attack",
        "phase_name": "privilege-escalation"
      }
    ],
    "modified": "2020-06-20T22:26:33.191Z",
    "name": "Extra Window Memory Injection",
    "object_marking_refs": [
      "marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168"
    ],
    "spec_version": "2.1",
    "type": "attack-pattern",
    "x_mitre_attack_spec_version": "2.1.0",
    "x_mitre_data_sources": [
      "Process monitoring",
      "API monitoring"
    ],
    "x_mitre_defense_bypassed": [
      "Anti-virus",
      "Application control"
    ],
    "x_mitre_detection": "Monitor for API calls related to enumerating and manipulating EWM such as GetWindowLong (Citation: Microsoft GetWindowLong function) and SetWindowLong (Citation: Microsoft SetWindowLong function). Malware associated with this technique have also used SendNotifyMessage (Citation: Microsoft SendNotifyMessage function) to trigger the associated window procedure and eventual malicious injection. (Citation: Endgame Process Injection July 2017)",
    "x_mitre_domains": [
      "enterprise-attack"
    ],
    "x_mitre_is_subtechnique": true,
    "x_mitre_modified_by_ref": "identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5",
    "x_mitre_platforms": [
      "Windows"
    ],
    "x_mitre_version": "1.0"
  },
  {
    "created": "2020-01-14T17:18:32.126Z",
    "created_by_ref": "identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5",
    "description": "Adversaries may inject malicious code into process via Extra Window Memory (EWM) in order to evade process-based defenses as well as possibly elevate privileges. EWM injection is a method of executing arbitrary code in the address space of a separate live process. \n\nBefore creating a window, graphical Windows-based processes must prescribe to or register a windows class, which stipulate appearance and behavior (via windows procedures, which are functions that handle input/output of data).(Citation: Microsoft Window Classes) Registration of new windows classes can include a request for up to 40 bytes of EWM to be appended to the allocated memory of each instance of that class. This EWM is intended to store data specific to that window and has specific application programming interface (API) functions to set and get its value. (Citation: Microsoft GetWindowLong function) (Citation: Microsoft SetWindowLong function)\n\nAlthough small, the EWM is large enough to store a 32-bit pointer and is often used to point to a windows procedure. Malware may possibly utilize this memory location in part of an attack chain that includes writing code to shared sections of the process’s memory, placing a pointer to the code in EWM, then invoking execution by returning execution control to the address in the process’s EWM.\n\nExecution granted through EWM injection may allow access to both the target process's memory and possibly elevated privileges. Writing payloads to shared sections also avoids the use of highly monitored API calls such as <code>WriteProcessMemory</code> and <code>CreateRemoteThread</code>.(Citation: Endgame Process Injection July 2017) More sophisticated malware samples may also potentially bypass protection mechanisms such as data execution prevention (DEP) by triggering a combination of windows procedures and other system functions that will rewrite the malicious payload inside an executable portion of the target process.  (Citation: MalwareTech Power Loader Aug 2013) (Citation: WeLiveSecurity Gapz and Redyms Mar 2013)\n\nRunning code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via EWM injection may also evade detection from security products since the execution is masked under a legitimate process. ",
    "external_references": [
      {
        "source_name": "mitre-attack",
        "external_id": "T1055.011",
        "url": "https://attack.mitre.org/techniques/T1055/011"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633574.aspx",
        "description": "Microsoft. (n.d.). About Window Classes. Retrieved December 16, 2017.",
        "source_name": "Microsoft Window Classes"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633584.aspx",
        "description": "Microsoft. (n.d.). GetWindowLong function. Retrieved December 16, 2017.",
        "source_name": "Microsoft GetWindowLong function"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633591.aspx",
        "description": "Microsoft. (n.d.). SetWindowLong function. Retrieved December 16, 2017.",
        "source_name": "Microsoft SetWindowLong function"
      },
      {
        "url": "https://www.endgame.com/blog/technical-blog/ten-process-injection-techniques-technical-survey-common-and-trending-process",
        "description": "Hosseini, A. (2017, July 18). Ten Process Injection Techniques: A Technical Survey Of Common And Trending Process Injection Techniques. Retrieved December 7, 2017.",
        "source_name": "Endgame Process Injection July 2017"
      },
      {
        "url": "https://www.malwaretech.com/2013/08/powerloader-injection-something-truly.html",
        "description": "MalwareTech. (2013, August 13). PowerLoader Injection – Something truly amazing. Retrieved December 16, 2017.",
        "source_name": "MalwareTech Power Loader Aug 2013"
      },
      {
        "url": "https://www.welivesecurity.com/2013/03/19/gapz-and-redyms-droppers-based-on-power-loader-code/",
        "description": "Matrosov, A. (2013, March 19). Gapz and Redyms droppers based on Power Loader code. Retrieved December 16, 2017.",
        "source_name": "WeLiveSecurity Gapz and Redyms Mar 2013"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms644953.aspx",
        "description": "Microsoft. (n.d.). SendNotifyMessage function. Retrieved December 16, 2017.",
        "source_name": "Microsoft SendNotifyMessage function"
      }
    ],
    "id": "attack-pattern--0042a9f5-f053-4769-b3ef-9ad018dfa298",
    "kill_chain_phases": [
      {
        "kill_chain_name": "mitre-attack",
        "phase_name": "defense-evasion"
      },
      {
        "kill_chain_name": "mitre-attack",
        "phase_name": "privilege-escalation"
      }
    ],
    "modified": "2020-06-20T22:26:33.191Z",
    "name": "Extra Window Memory Injection",
    "object_marking_refs": [
      "marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168"
    ],
    "spec_version": "2.1",
    "type": "attack-pattern",
    "x_mitre_attack_spec_version": "2.1.0",
    "x_mitre_data_sources": [
      "Process monitoring",
      "API monitoring"
    ],
    "x_mitre_defense_bypassed": [
      "Anti-virus",
      "Application control"
    ],
    "x_mitre_detection": "Monitor for API calls related to enumerating and manipulating EWM such as GetWindowLong (Citation: Microsoft GetWindowLong function) and SetWindowLong (Citation: Microsoft SetWindowLong function). Malware associated with this technique have also used SendNotifyMessage (Citation: Microsoft SendNotifyMessage function) to trigger the associated window procedure and eventual malicious injection. (Citation: Endgame Process Injection July 2017)",
    "x_mitre_domains": [
      "enterprise-attack"
    ],
    "x_mitre_is_subtechnique": true,
    "x_mitre_modified_by_ref": "identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5",
    "x_mitre_platforms": [
      "Windows"
    ],
    "x_mitre_version": "1.0"
  },
  {
    "created": "2020-01-14T17:18:32.126Z",
    "created_by_ref": "identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5",
    "description": "Adversaries may inject malicious code into process via Extra Window Memory (EWM) in order to evade process-based defenses as well as possibly elevate privileges. EWM injection is a method of executing arbitrary code in the address space of a separate live process. \n\nBefore creating a window, graphical Windows-based processes must prescribe to or register a windows class, which stipulate appearance and behavior (via windows procedures, which are functions that handle input/output of data).(Citation: Microsoft Window Classes) Registration of new windows classes can include a request for up to 40 bytes of EWM to be appended to the allocated memory of each instance of that class. This EWM is intended to store data specific to that window and has specific application programming interface (API) functions to set and get its value. (Citation: Microsoft GetWindowLong function) (Citation: Microsoft SetWindowLong function)\n\nAlthough small, the EWM is large enough to store a 32-bit pointer and is often used to point to a windows procedure. Malware may possibly utilize this memory location in part of an attack chain that includes writing code to shared sections of the process’s memory, placing a pointer to the code in EWM, then invoking execution by returning execution control to the address in the process’s EWM.\n\nExecution granted through EWM injection may allow access to both the target process's memory and possibly elevated privileges. Writing payloads to shared sections also avoids the use of highly monitored API calls such as <code>WriteProcessMemory</code> and <code>CreateRemoteThread</code>.(Citation: Endgame Process Injection July 2017) More sophisticated malware samples may also potentially bypass protection mechanisms such as data execution prevention (DEP) by triggering a combination of windows procedures and other system functions that will rewrite the malicious payload inside an executable portion of the target process.  (Citation: MalwareTech Power Loader Aug 2013) (Citation: WeLiveSecurity Gapz and Redyms Mar 2013)\n\nRunning code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via EWM injection may also evade detection from security products since the execution is masked under a legitimate process. ",
    "external_references": [
      {
        "source_name": "mitre-attack",
        "external_id": "T1055.011",
        "url": "https://attack.mitre.org/techniques/T1055/011"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633574.aspx",
        "description": "Microsoft. (n.d.). About Window Classes. Retrieved December 16, 2017.",
        "source_name": "Microsoft Window Classes"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633584.aspx",
        "description": "Microsoft. (n.d.). GetWindowLong function. Retrieved December 16, 2017.",
        "source_name": "Microsoft GetWindowLong function"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633591.aspx",
        "description": "Microsoft. (n.d.). SetWindowLong function. Retrieved December 16, 2017.",
        "source_name": "Microsoft SetWindowLong function"
      },
      {
        "url": "https://www.endgame.com/blog/technical-blog/ten-process-injection-techniques-technical-survey-common-and-trending-process",
        "description": "Hosseini, A. (2017, July 18). Ten Process Injection Techniques: A Technical Survey Of Common And Trending Process Injection Techniques. Retrieved December 7, 2017.",
        "source_name": "Endgame Process Injection July 2017"
      },
      {
        "url": "https://www.malwaretech.com/2013/08/powerloader-injection-something-truly.html",
        "description": "MalwareTech. (2013, August 13). PowerLoader Injection – Something truly amazing. Retrieved December 16, 2017.",
        "source_name": "MalwareTech Power Loader Aug 2013"
      },
      {
        "url": "https://www.welivesecurity.com/2013/03/19/gapz-and-redyms-droppers-based-on-power-loader-code/",
        "description": "Matrosov, A. (2013, March 19). Gapz and Redyms droppers based on Power Loader code. Retrieved December 16, 2017.",
        "source_name": "WeLiveSecurity Gapz and Redyms Mar 2013"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms644953.aspx",
        "description": "Microsoft. (n.d.). SendNotifyMessage function. Retrieved December 16, 2017.",
        "source_name": "Microsoft SendNotifyMessage function"
      }
    ],
    "id": "attack-pattern--0042a9f5-f053-4769-b3ef-9ad018dfa298",
    "kill_chain_phases": [
      {
        "kill_chain_name": "mitre-attack",
        "phase_name": "defense-evasion"
      },
      {
        "kill_chain_name": "mitre-attack",
        "phase_name": "privilege-escalation"
      }
    ],
    "modified": "2020-06-20T22:26:33.191Z",
    "name": "Extra Window Memory Injection",
    "object_marking_refs": [
      "marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168"
    ],
    "spec_version": "2.1",
    "type": "attack-pattern",
    "x_mitre_attack_spec_version": "2.1.0",
    "x_mitre_data_sources": [
      "Process monitoring",
      "API monitoring"
    ],
    "x_mitre_defense_bypassed": [
      "Anti-virus",
      "Application control"
    ],
    "x_mitre_detection": "Monitor for API calls related to enumerating and manipulating EWM such as GetWindowLong (Citation: Microsoft GetWindowLong function) and SetWindowLong (Citation: Microsoft SetWindowLong function). Malware associated with this technique have also used SendNotifyMessage (Citation: Microsoft SendNotifyMessage function) to trigger the associated window procedure and eventual malicious injection. (Citation: Endgame Process Injection July 2017)",
    "x_mitre_domains": [
      "enterprise-attack"
    ],
    "x_mitre_is_subtechnique": true,
    "x_mitre_modified_by_ref": "identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5",
    "x_mitre_platforms": [
      "Windows"
    ],
    "x_mitre_version": "1.0"
  },
  {
    "created": "2020-01-14T17:18:32.126Z",
    "created_by_ref": "identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5",
    "description": "Adversaries may inject malicious code into process via Extra Window Memory (EWM) in order to evade process-based defenses as well as possibly elevate privileges. EWM injection is a method of executing arbitrary code in the address space of a separate live process. \n\nBefore creating a window, graphical Windows-based processes must prescribe to or register a windows class, which stipulate appearance and behavior (via windows procedures, which are functions that handle input/output of data).(Citation: Microsoft Window Classes) Registration of new windows classes can include a request for up to 40 bytes of EWM to be appended to the allocated memory of each instance of that class. This EWM is intended to store data specific to that window and has specific application programming interface (API) functions to set and get its value. (Citation: Microsoft GetWindowLong function) (Citation: Microsoft SetWindowLong function)\n\nAlthough small, the EWM is large enough to store a 32-bit pointer and is often used to point to a windows procedure. Malware may possibly utilize this memory location in part of an attack chain that includes writing code to shared sections of the process’s memory, placing a pointer to the code in EWM, then invoking execution by returning execution control to the address in the process’s EWM.\n\nExecution granted through EWM injection may allow access to both the target process's memory and possibly elevated privileges. Writing payloads to shared sections also avoids the use of highly monitored API calls such as <code>WriteProcessMemory</code> and <code>CreateRemoteThread</code>.(Citation: Endgame Process Injection July 2017) More sophisticated malware samples may also potentially bypass protection mechanisms such as data execution prevention (DEP) by triggering a combination of windows procedures and other system functions that will rewrite the malicious payload inside an executable portion of the target process.  (Citation: MalwareTech Power Loader Aug 2013) (Citation: WeLiveSecurity Gapz and Redyms Mar 2013)\n\nRunning code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via EWM injection may also evade detection from security products since the execution is masked under a legitimate process. ",
    "external_references": [
      {
        "source_name": "mitre-attack",
        "external_id": "T1055.011",
        "url": "https://attack.mitre.org/techniques/T1055/011"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633574.aspx",
        "description": "Microsoft. (n.d.). About Window Classes. Retrieved December 16, 2017.",
        "source_name": "Microsoft Window Classes"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633584.aspx",
        "description": "Microsoft. (n.d.). GetWindowLong function. Retrieved December 16, 2017.",
        "source_name": "Microsoft GetWindowLong function"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633591.aspx",
        "description": "Microsoft. (n.d.). SetWindowLong function. Retrieved December 16, 2017.",
        "source_name": "Microsoft SetWindowLong function"
      },
      {
        "url": "https://www.endgame.com/blog/technical-blog/ten-process-injection-techniques-technical-survey-common-and-trending-process",
        "description": "Hosseini, A. (2017, July 18). Ten Process Injection Techniques: A Technical Survey Of Common And Trending Process Injection Techniques. Retrieved December 7, 2017.",
        "source_name": "Endgame Process Injection July 2017"
      },
      {
        "url": "https://www.malwaretech.com/2013/08/powerloader-injection-something-truly.html",
        "description": "MalwareTech. (2013, August 13). PowerLoader Injection – Something truly amazing. Retrieved December 16, 2017.",
        "source_name": "MalwareTech Power Loader Aug 2013"
      },
      {
        "url": "https://www.welivesecurity.com/2013/03/19/gapz-and-redyms-droppers-based-on-power-loader-code/",
        "description": "Matrosov, A. (2013, March 19). Gapz and Redyms droppers based on Power Loader code. Retrieved December 16, 2017.",
        "source_name": "WeLiveSecurity Gapz and Redyms Mar 2013"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms644953.aspx",
        "description": "Microsoft. (n.d.). SendNotifyMessage function. Retrieved December 16, 2017.",
        "source_name": "Microsoft SendNotifyMessage function"
      }
    ],
    "id": "attack-pattern--0042a9f5-f053-4769-b3ef-9ad018dfa298",
    "kill_chain_phases": [
      {
        "kill_chain_name": "mitre-attack",
        "phase_name": "defense-evasion"
      },
      {
        "kill_chain_name": "mitre-attack",
        "phase_name": "privilege-escalation"
      }
    ],
    "modified": "2020-06-20T22:26:33.191Z",
    "name": "Extra Window Memory Injection",
    "object_marking_refs": [
      "marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168"
    ],
    "spec_version": "2.1",
    "type": "attack-pattern",
    "x_mitre_attack_spec_version": "2.1.0",
    "x_mitre_data_sources": [
      "Process monitoring",
      "API monitoring"
    ],
    "x_mitre_defense_bypassed": [
      "Anti-virus",
      "Application control"
    ],
    "x_mitre_detection": "Monitor for API calls related to enumerating and manipulating EWM such as GetWindowLong (Citation: Microsoft GetWindowLong function) and SetWindowLong (Citation: Microsoft SetWindowLong function). Malware associated with this technique have also used SendNotifyMessage (Citation: Microsoft SendNotifyMessage function) to trigger the associated window procedure and eventual malicious injection. (Citation: Endgame Process Injection July 2017)",
    "x_mitre_domains": [
      "enterprise-attack"
    ],
    "x_mitre_is_subtechnique": true,
    "x_mitre_modified_by_ref": "identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5",
    "x_mitre_platforms": [
      "Windows"
    ],
    "x_mitre_version": "1.0"
  },
  {
    "created": "2020-01-14T17:18:32.126Z",
    "created_by_ref": "identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5",
    "description": "Adversaries may inject malicious code into process via Extra Window Memory (EWM) in order to evade process-based defenses as well as possibly elevate privileges. EWM injection is a method of executing arbitrary code in the address space of a separate live process. \n\nBefore creating a window, graphical Windows-based processes must prescribe to or register a windows class, which stipulate appearance and behavior (via windows procedures, which are functions that handle input/output of data).(Citation: Microsoft Window Classes) Registration of new windows classes can include a request for up to 40 bytes of EWM to be appended to the allocated memory of each instance of that class. This EWM is intended to store data specific to that window and has specific application programming interface (API) functions to set and get its value. (Citation: Microsoft GetWindowLong function) (Citation: Microsoft SetWindowLong function)\n\nAlthough small, the EWM is large enough to store a 32-bit pointer and is often used to point to a windows procedure. Malware may possibly utilize this memory location in part of an attack chain that includes writing code to shared sections of the process’s memory, placing a pointer to the code in EWM, then invoking execution by returning execution control to the address in the process’s EWM.\n\nExecution granted through EWM injection may allow access to both the target process's memory and possibly elevated privileges. Writing payloads to shared sections also avoids the use of highly monitored API calls such as <code>WriteProcessMemory</code> and <code>CreateRemoteThread</code>.(Citation: Endgame Process Injection July 2017) More sophisticated malware samples may also potentially bypass protection mechanisms such as data execution prevention (DEP) by triggering a combination of windows procedures and other system functions that will rewrite the malicious payload inside an executable portion of the target process.  (Citation: MalwareTech Power Loader Aug 2013) (Citation: WeLiveSecurity Gapz and Redyms Mar 2013)\n\nRunning code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via EWM injection may also evade detection from security products since the execution is masked under a legitimate process. ",
    "external_references": [
      {
        "source_name": "mitre-attack",
        "external_id": "T1055.011",
        "url": "https://attack.mitre.org/techniques/T1055/011"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633574.aspx",
        "description": "Microsoft. (n.d.). About Window Classes. Retrieved December 16, 2017.",
        "source_name": "Microsoft Window Classes"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633584.aspx",
        "description": "Microsoft. (n.d.). GetWindowLong function. Retrieved December 16, 2017.",
        "source_name": "Microsoft GetWindowLong function"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633591.aspx",
        "description": "Microsoft. (n.d.). SetWindowLong function. Retrieved December 16, 2017.",
        "source_name": "Microsoft SetWindowLong function"
      },
      {
        "url": "https://www.endgame.com/blog/technical-blog/ten-process-injection-techniques-technical-survey-common-and-trending-process",
        "description": "Hosseini, A. (2017, July 18). Ten Process Injection Techniques: A Technical Survey Of Common And Trending Process Injection Techniques. Retrieved December 7, 2017.",
        "source_name": "Endgame Process Injection July 2017"
      },
      {
        "url": "https://www.malwaretech.com/2013/08/powerloader-injection-something-truly.html",
        "description": "MalwareTech. (2013, August 13). PowerLoader Injection – Something truly amazing. Retrieved December 16, 2017.",
        "source_name": "MalwareTech Power Loader Aug 2013"
      },
      {
        "url": "https://www.welivesecurity.com/2013/03/19/gapz-and-redyms-droppers-based-on-power-loader-code/",
        "description": "Matrosov, A. (2013, March 19). Gapz and Redyms droppers based on Power Loader code. Retrieved December 16, 2017.",
        "source_name": "WeLiveSecurity Gapz and Redyms Mar 2013"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms644953.aspx",
        "description": "Microsoft. (n.d.). SendNotifyMessage function. Retrieved December 16, 2017.",
        "source_name": "Microsoft SendNotifyMessage function"
      }
    ],
    "id": "attack-pattern--0042a9f5-f053-4769-b3ef-9ad018dfa298",
    "kill_chain_phases": [
      {
        "kill_chain_name": "mitre-attack",
        "phase_name": "defense-evasion"
      },
      {
        "kill_chain_name": "mitre-attack",
        "phase_name": "privilege-escalation"
      }
    ],
    "modified": "2020-06-20T22:26:33.191Z",
    "name": "Extra Window Memory Injection",
    "object_marking_refs": [
      "marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168"
    ],
    "spec_version": "2.1",
    "type": "attack-pattern",
    "x_mitre_attack_spec_version": "2.1.0",
    "x_mitre_data_sources": [
      "Process monitoring",
      "API monitoring"
    ],
    "x_mitre_defense_bypassed": [
      "Anti-virus",
      "Application control"
    ],
    "x_mitre_detection": "Monitor for API calls related to enumerating and manipulating EWM such as GetWindowLong (Citation: Microsoft GetWindowLong function) and SetWindowLong (Citation: Microsoft SetWindowLong function). Malware associated with this technique have also used SendNotifyMessage (Citation: Microsoft SendNotifyMessage function) to trigger the associated window procedure and eventual malicious injection. (Citation: Endgame Process Injection July 2017)",
    "x_mitre_domains": [
      "enterprise-attack"
    ],
    "x_mitre_is_subtechnique": true,
    "x_mitre_modified_by_ref": "identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5",
    "x_mitre_platforms": [
      "Windows"
    ],
    "x_mitre_version": "1.0"
  },
  {
    "created": "2020-01-14T17:18:32.126Z",
    "created_by_ref": "identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5",
    "description": "Adversaries may inject malicious code into process via Extra Window Memory (EWM) in order to evade process-based defenses as well as possibly elevate privileges. EWM injection is a method of executing arbitrary code in the address space of a separate live process. \n\nBefore creating a window, graphical Windows-based processes must prescribe to or register a windows class, which stipulate appearance and behavior (via windows procedures, which are functions that handle input/output of data).(Citation: Microsoft Window Classes) Registration of new windows classes can include a request for up to 40 bytes of EWM to be appended to the allocated memory of each instance of that class. This EWM is intended to store data specific to that window and has specific application programming interface (API) functions to set and get its value. (Citation: Microsoft GetWindowLong function) (Citation: Microsoft SetWindowLong function)\n\nAlthough small, the EWM is large enough to store a 32-bit pointer and is often used to point to a windows procedure. Malware may possibly utilize this memory location in part of an attack chain that includes writing code to shared sections of the process’s memory, placing a pointer to the code in EWM, then invoking execution by returning execution control to the address in the process’s EWM.\n\nExecution granted through EWM injection may allow access to both the target process's memory and possibly elevated privileges. Writing payloads to shared sections also avoids the use of highly monitored API calls such as <code>WriteProcessMemory</code> and <code>CreateRemoteThread</code>.(Citation: Endgame Process Injection July 2017) More sophisticated malware samples may also potentially bypass protection mechanisms such as data execution prevention (DEP) by triggering a combination of windows procedures and other system functions that will rewrite the malicious payload inside an executable portion of the target process.  (Citation: MalwareTech Power Loader Aug 2013) (Citation: WeLiveSecurity Gapz and Redyms Mar 2013)\n\nRunning code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via EWM injection may also evade detection from security products since the execution is masked under a legitimate process. ",
    "external_references": [
      {
        "source_name": "mitre-attack",
        "external_id": "T1055.011",
        "url": "https://attack.mitre.org/techniques/T1055/011"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633574.aspx",
        "description": "Microsoft. (n.d.). About Window Classes. Retrieved December 16, 2017.",
        "source_name": "Microsoft Window Classes"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633584.aspx",
        "description": "Microsoft. (n.d.). GetWindowLong function. Retrieved December 16, 2017.",
        "source_name": "Microsoft GetWindowLong function"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633591.aspx",
        "description": "Microsoft. (n.d.). SetWindowLong function. Retrieved December 16, 2017.",
        "source_name": "Microsoft SetWindowLong function"
      },
      {
        "url": "https://www.endgame.com/blog/technical-blog/ten-process-injection-techniques-technical-survey-common-and-trending-process",
        "description": "Hosseini, A. (2017, July 18). Ten Process Injection Techniques: A Technical Survey Of Common And Trending Process Injection Techniques. Retrieved December 7, 2017.",
        "source_name": "Endgame Process Injection July 2017"
      },
      {
        "url": "https://www.malwaretech.com/2013/08/powerloader-injection-something-truly.html",
        "description": "MalwareTech. (2013, August 13). PowerLoader Injection – Something truly amazing. Retrieved December 16, 2017.",
        "source_name": "MalwareTech Power Loader Aug 2013"
      },
      {
        "url": "https://www.welivesecurity.com/2013/03/19/gapz-and-redyms-droppers-based-on-power-loader-code/",
        "description": "Matrosov, A. (2013, March 19). Gapz and Redyms droppers based on Power Loader code. Retrieved December 16, 2017.",
        "source_name": "WeLiveSecurity Gapz and Redyms Mar 2013"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms644953.aspx",
        "description": "Microsoft. (n.d.). SendNotifyMessage function. Retrieved December 16, 2017.",
        "source_name": "Microsoft SendNotifyMessage function"
      }
    ],
    "id": "attack-pattern--0042a9f5-f053-4769-b3ef-9ad018dfa298",
    "kill_chain_phases": [
      {
        "kill_chain_name": "mitre-attack",
        "phase_name": "defense-evasion"
      },
      {
        "kill_chain_name": "mitre-attack",
        "phase_name": "privilege-escalation"
      }
    ],
    "modified": "2020-06-20T22:26:33.191Z",
    "name": "Extra Window Memory Injection",
    "object_marking_refs": [
      "marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168"
    ],
    "spec_version": "2.1",
    "type": "attack-pattern",
    "x_mitre_attack_spec_version": "2.1.0",
    "x_mitre_data_sources": [
      "Process monitoring",
      "API monitoring"
    ],
    "x_mitre_defense_bypassed": [
      "Anti-virus",
      "Application control"
    ],
    "x_mitre_detection": "Monitor for API calls related to enumerating and manipulating EWM such as GetWindowLong (Citation: Microsoft GetWindowLong function) and SetWindowLong (Citation: Microsoft SetWindowLong function). Malware associated with this technique have also used SendNotifyMessage (Citation: Microsoft SendNotifyMessage function) to trigger the associated window procedure and eventual malicious injection. (Citation: Endgame Process Injection July 2017)",
    "x_mitre_domains": [
      "enterprise-attack"
    ],
    "x_mitre_is_subtechnique": true,
    "x_mitre_modified_by_ref": "identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5",
    "x_mitre_platforms": [
      "Windows"
    ],
    "x_mitre_version": "1.0"
  },
  {
    "created": "2020-01-14T17:18:32.126Z",
    "created_by_ref": "identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5",
    "description": "Adversaries may inject malicious code into process via Extra Window Memory (EWM) in order to evade process-based defenses as well as possibly elevate privileges. EWM injection is a method of executing arbitrary code in the address space of a separate live process. \n\nBefore creating a window, graphical Windows-based processes must prescribe to or register a windows class, which stipulate appearance and behavior (via windows procedures, which are functions that handle input/output of data).(Citation: Microsoft Window Classes) Registration of new windows classes can include a request for up to 40 bytes of EWM to be appended to the allocated memory of each instance of that class. This EWM is intended to store data specific to that window and has specific application programming interface (API) functions to set and get its value. (Citation: Microsoft GetWindowLong function) (Citation: Microsoft SetWindowLong function)\n\nAlthough small, the EWM is large enough to store a 32-bit pointer and is often used to point to a windows procedure. Malware may possibly utilize this memory location in part of an attack chain that includes writing code to shared sections of the process’s memory, placing a pointer to the code in EWM, then invoking execution by returning execution control to the address in the process’s EWM.\n\nExecution granted through EWM injection may allow access to both the target process's memory and possibly elevated privileges. Writing payloads to shared sections also avoids the use of highly monitored API calls such as <code>WriteProcessMemory</code> and <code>CreateRemoteThread</code>.(Citation: Elastic Process Injection July 2017) More sophisticated malware samples may also potentially bypass protection mechanisms such as data execution prevention (DEP) by triggering a combination of windows procedures and other system functions that will rewrite the malicious payload inside an executable portion of the target process.  (Citation: MalwareTech Power Loader Aug 2013) (Citation: WeLiveSecurity Gapz and Redyms Mar 2013)\n\nRunning code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via EWM injection may also evade detection from security products since the execution is masked under a legitimate process. ",
    "external_references": [
      {
        "source_name": "mitre-attack",
        "external_id": "T1055.011",
        "url": "https://attack.mitre.org/techniques/T1055/011"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633574.aspx",
        "description": "Microsoft. (n.d.). About Window Classes. Retrieved December 16, 2017.",
        "source_name": "Microsoft Window Classes"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633584.aspx",
        "description": "Microsoft. (n.d.). GetWindowLong function. Retrieved December 16, 2017.",
        "source_name": "Microsoft GetWindowLong function"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633591.aspx",
        "description": "Microsoft. (n.d.). SetWindowLong function. Retrieved December 16, 2017.",
        "source_name": "Microsoft SetWindowLong function"
      },
      {
        "url": "https://www.endgame.com/blog/technical-blog/ten-process-injection-techniques-technical-survey-common-and-trending-process",
        "description": "Hosseini, A. (2017, July 18). Ten Process Injection Techniques: A Technical Survey Of Common And Trending Process Injection Techniques. Retrieved December 7, 2017.",
        "source_name": "Elastic Process Injection July 2017"
      },
      {
        "url": "https://www.malwaretech.com/2013/08/powerloader-injection-something-truly.html",
        "description": "MalwareTech. (2013, August 13). PowerLoader Injection – Something truly amazing. Retrieved December 16, 2017.",
        "source_name": "MalwareTech Power Loader Aug 2013"
      },
      {
        "url": "https://www.welivesecurity.com/2013/03/19/gapz-and-redyms-droppers-based-on-power-loader-code/",
        "description": "Matrosov, A. (2013, March 19). Gapz and Redyms droppers based on Power Loader code. Retrieved December 16, 2017.",
        "source_name": "WeLiveSecurity Gapz and Redyms Mar 2013"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms644953.aspx",
        "description": "Microsoft. (n.d.). SendNotifyMessage function. Retrieved December 16, 2017.",
        "source_name": "Microsoft SendNotifyMessage function"
      }
    ],
    "id": "attack-pattern--0042a9f5-f053-4769-b3ef-9ad018dfa298",
    "kill_chain_phases": [
      {
        "kill_chain_name": "mitre-attack",
        "phase_name": "defense-evasion"
      },
      {
        "kill_chain_name": "mitre-attack",
        "phase_name": "privilege-escalation"
      }
    ],
    "modified": "2020-11-10T18:29:31.004Z",
    "name": "Extra Window Memory Injection",
    "object_marking_refs": [
      "marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168"
    ],
    "spec_version": "2.1",
    "type": "attack-pattern",
    "x_mitre_attack_spec_version": "2.1.0",
    "x_mitre_data_sources": [
      "Process: OS API Execution"
    ],
    "x_mitre_defense_bypassed": [
      "Anti-virus",
      "Application control"
    ],
    "x_mitre_detection": "Monitor for API calls related to enumerating and manipulating EWM such as GetWindowLong (Citation: Microsoft GetWindowLong function) and SetWindowLong (Citation: Microsoft SetWindowLong function). Malware associated with this technique have also used SendNotifyMessage (Citation: Microsoft SendNotifyMessage function) to trigger the associated window procedure and eventual malicious injection. (Citation: Elastic Process Injection July 2017)",
    "x_mitre_domains": [
      "enterprise-attack"
    ],
    "x_mitre_is_subtechnique": true,
    "x_mitre_modified_by_ref": "identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5",
    "x_mitre_platforms": [
      "Windows"
    ],
    "x_mitre_version": "1.0"
  },
  {
    "created": "2020-01-14T17:18:32.126Z",
    "created_by_ref": "identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5",
    "description": "Adversaries may inject malicious code into process via Extra Window Memory (EWM) in order to evade process-based defenses as well as possibly elevate privileges. EWM injection is a method of executing arbitrary code in the address space of a separate live process. \n\nBefore creating a window, graphical Windows-based processes must prescribe to or register a windows class, which stipulate appearance and behavior (via windows procedures, which are functions that handle input/output of data).(Citation: Microsoft Window Classes) Registration of new windows classes can include a request for up to 40 bytes of EWM to be appended to the allocated memory of each instance of that class. This EWM is intended to store data specific to that window and has specific application programming interface (API) functions to set and get its value. (Citation: Microsoft GetWindowLong function) (Citation: Microsoft SetWindowLong function)\n\nAlthough small, the EWM is large enough to store a 32-bit pointer and is often used to point to a windows procedure. Malware may possibly utilize this memory location in part of an attack chain that includes writing code to shared sections of the process’s memory, placing a pointer to the code in EWM, then invoking execution by returning execution control to the address in the process’s EWM.\n\nExecution granted through EWM injection may allow access to both the target process's memory and possibly elevated privileges. Writing payloads to shared sections also avoids the use of highly monitored API calls such as <code>WriteProcessMemory</code> and <code>CreateRemoteThread</code>.(Citation: Elastic Process Injection July 2017) More sophisticated malware samples may also potentially bypass protection mechanisms such as data execution prevention (DEP) by triggering a combination of windows procedures and other system functions that will rewrite the malicious payload inside an executable portion of the target process.  (Citation: MalwareTech Power Loader Aug 2013) (Citation: WeLiveSecurity Gapz and Redyms Mar 2013)\n\nRunning code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via EWM injection may also evade detection from security products since the execution is masked under a legitimate process. ",
    "external_references": [
      {
        "source_name": "mitre-attack",
        "external_id": "T1055.011",
        "url": "https://attack.mitre.org/techniques/T1055/011"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633574.aspx",
        "description": "Microsoft. (n.d.). About Window Classes. Retrieved December 16, 2017.",
        "source_name": "Microsoft Window Classes"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633584.aspx",
        "description": "Microsoft. (n.d.). GetWindowLong function. Retrieved December 16, 2017.",
        "source_name": "Microsoft GetWindowLong function"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633591.aspx",
        "description": "Microsoft. (n.d.). SetWindowLong function. Retrieved December 16, 2017.",
        "source_name": "Microsoft SetWindowLong function"
      },
      {
        "url": "https://www.endgame.com/blog/technical-blog/ten-process-injection-techniques-technical-survey-common-and-trending-process",
        "description": "Hosseini, A. (2017, July 18). Ten Process Injection Techniques: A Technical Survey Of Common And Trending Process Injection Techniques. Retrieved December 7, 2017.",
        "source_name": "Elastic Process Injection July 2017"
      },
      {
        "url": "https://www.malwaretech.com/2013/08/powerloader-injection-something-truly.html",
        "description": "MalwareTech. (2013, August 13). PowerLoader Injection – Something truly amazing. Retrieved December 16, 2017.",
        "source_name": "MalwareTech Power Loader Aug 2013"
      },
      {
        "url": "https://www.welivesecurity.com/2013/03/19/gapz-and-redyms-droppers-based-on-power-loader-code/",
        "description": "Matrosov, A. (2013, March 19). Gapz and Redyms droppers based on Power Loader code. Retrieved December 16, 2017.",
        "source_name": "WeLiveSecurity Gapz and Redyms Mar 2013"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms644953.aspx",
        "description": "Microsoft. (n.d.). SendNotifyMessage function. Retrieved December 16, 2017.",
        "source_name": "Microsoft SendNotifyMessage function"
      }
    ],
    "id": "attack-pattern--0042a9f5-f053-4769-b3ef-9ad018dfa298",
    "kill_chain_phases": [
      {
        "kill_chain_name": "mitre-attack",
        "phase_name": "defense-evasion"
      },
      {
        "kill_chain_name": "mitre-attack",
        "phase_name": "privilege-escalation"
      }
    ],
    "modified": "2020-11-10T18:29:31.004Z",
    "name": "Extra Window Memory Injection",
    "object_marking_refs": [
      "marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168"
    ],
    "spec_version": "2.1",
    "type": "attack-pattern",
    "x_mitre_attack_spec_version": "2.1.0",
    "x_mitre_data_sources": [
      "Process: OS API Execution"
    ],
    "x_mitre_defense_bypassed": [
      "Anti-virus",
      "Application control"
    ],
    "x_mitre_detection": "Monitor for API calls related to enumerating and manipulating EWM such as GetWindowLong (Citation: Microsoft GetWindowLong function) and SetWindowLong (Citation: Microsoft SetWindowLong function). Malware associated with this technique have also used SendNotifyMessage (Citation: Microsoft SendNotifyMessage function) to trigger the associated window procedure and eventual malicious injection. (Citation: Elastic Process Injection July 2017)",
    "x_mitre_domains": [
      "enterprise-attack"
    ],
    "x_mitre_is_subtechnique": true,
    "x_mitre_modified_by_ref": "identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5",
    "x_mitre_platforms": [
      "Windows"
    ],
    "x_mitre_version": "1.0"
  },
  {
    "created": "2020-01-14T17:18:32.126Z",
    "created_by_ref": "identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5",
    "description": "Adversaries may inject malicious code into process via Extra Window Memory (EWM) in order to evade process-based defenses as well as possibly elevate privileges. EWM injection is a method of executing arbitrary code in the address space of a separate live process. \n\nBefore creating a window, graphical Windows-based processes must prescribe to or register a windows class, which stipulate appearance and behavior (via windows procedures, which are functions that handle input/output of data).(Citation: Microsoft Window Classes) Registration of new windows classes can include a request for up to 40 bytes of EWM to be appended to the allocated memory of each instance of that class. This EWM is intended to store data specific to that window and has specific application programming interface (API) functions to set and get its value. (Citation: Microsoft GetWindowLong function) (Citation: Microsoft SetWindowLong function)\n\nAlthough small, the EWM is large enough to store a 32-bit pointer and is often used to point to a windows procedure. Malware may possibly utilize this memory location in part of an attack chain that includes writing code to shared sections of the process’s memory, placing a pointer to the code in EWM, then invoking execution by returning execution control to the address in the process’s EWM.\n\nExecution granted through EWM injection may allow access to both the target process's memory and possibly elevated privileges. Writing payloads to shared sections also avoids the use of highly monitored API calls such as <code>WriteProcessMemory</code> and <code>CreateRemoteThread</code>.(Citation: Elastic Process Injection July 2017) More sophisticated malware samples may also potentially bypass protection mechanisms such as data execution prevention (DEP) by triggering a combination of windows procedures and other system functions that will rewrite the malicious payload inside an executable portion of the target process.  (Citation: MalwareTech Power Loader Aug 2013) (Citation: WeLiveSecurity Gapz and Redyms Mar 2013)\n\nRunning code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via EWM injection may also evade detection from security products since the execution is masked under a legitimate process. ",
    "external_references": [
      {
        "url": "https://attack.mitre.org/techniques/T1055/011",
        "external_id": "T1055.011",
        "source_name": "mitre-attack"
      },
      {
        "source_name": "Microsoft Window Classes",
        "description": "Microsoft. (n.d.). About Window Classes. Retrieved December 16, 2017.",
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633574.aspx"
      },
      {
        "source_name": "Microsoft GetWindowLong function",
        "description": "Microsoft. (n.d.). GetWindowLong function. Retrieved December 16, 2017.",
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633584.aspx"
      },
      {
        "source_name": "Microsoft SetWindowLong function",
        "description": "Microsoft. (n.d.). SetWindowLong function. Retrieved December 16, 2017.",
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633591.aspx"
      },
      {
        "source_name": "Elastic Process Injection July 2017",
        "description": "Hosseini, A. (2017, July 18). Ten Process Injection Techniques: A Technical Survey Of Common And Trending Process Injection Techniques. Retrieved December 7, 2017.",
        "url": "https://www.endgame.com/blog/technical-blog/ten-process-injection-techniques-technical-survey-common-and-trending-process"
      },
      {
        "source_name": "MalwareTech Power Loader Aug 2013",
        "description": "MalwareTech. (2013, August 13). PowerLoader Injection – Something truly amazing. Retrieved December 16, 2017.",
        "url": "https://www.malwaretech.com/2013/08/powerloader-injection-something-truly.html"
      },
      {
        "source_name": "WeLiveSecurity Gapz and Redyms Mar 2013",
        "description": "Matrosov, A. (2013, March 19). Gapz and Redyms droppers based on Power Loader code. Retrieved December 16, 2017.",
        "url": "https://www.welivesecurity.com/2013/03/19/gapz-and-redyms-droppers-based-on-power-loader-code/"
      },
      {
        "source_name": "Microsoft SendNotifyMessage function",
        "description": "Microsoft. (n.d.). SendNotifyMessage function. Retrieved December 16, 2017.",
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms644953.aspx"
      }
    ],
    "id": "attack-pattern--0042a9f5-f053-4769-b3ef-9ad018dfa298",
    "kill_chain_phases": [
      {
        "kill_chain_name": "mitre-attack",
        "phase_name": "defense-evasion"
      },
      {
        "kill_chain_name": "mitre-attack",
        "phase_name": "privilege-escalation"
      }
    ],
    "modified": "2020-11-10T18:29:31.004Z",
    "name": "Extra Window Memory Injection",
    "object_marking_refs": [
      "marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168"
    ],
    "spec_version": "2.1",
    "type": "attack-pattern",
    "x_mitre_attack_spec_version": "2.1.0",
    "x_mitre_data_sources": [
      "Process: OS API Execution"
    ],
    "x_mitre_defense_bypassed": [
      "Anti-virus",
      "Application control"
    ],
    "x_mitre_detection": "Monitor for API calls related to enumerating and manipulating EWM such as GetWindowLong (Citation: Microsoft GetWindowLong function) and SetWindowLong (Citation: Microsoft SetWindowLong function). Malware associated with this technique have also used SendNotifyMessage (Citation: Microsoft SendNotifyMessage function) to trigger the associated window procedure and eventual malicious injection. (Citation: Elastic Process Injection July 2017)",
    "x_mitre_domains": [
      "enterprise-attack"
    ],
    "x_mitre_is_subtechnique": true,
    "x_mitre_modified_by_ref": "identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5",
    "x_mitre_platforms": [
      "Windows"
    ],
    "x_mitre_version": "1.0"
  },
  {
    "created": "2020-01-14T17:18:32.126Z",
    "created_by_ref": "identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5",
    "description": "Adversaries may inject malicious code into process via Extra Window Memory (EWM) in order to evade process-based defenses as well as possibly elevate privileges. EWM injection is a method of executing arbitrary code in the address space of a separate live process. \n\nBefore creating a window, graphical Windows-based processes must prescribe to or register a windows class, which stipulate appearance and behavior (via windows procedures, which are functions that handle input/output of data).(Citation: Microsoft Window Classes) Registration of new windows classes can include a request for up to 40 bytes of EWM to be appended to the allocated memory of each instance of that class. This EWM is intended to store data specific to that window and has specific application programming interface (API) functions to set and get its value. (Citation: Microsoft GetWindowLong function) (Citation: Microsoft SetWindowLong function)\n\nAlthough small, the EWM is large enough to store a 32-bit pointer and is often used to point to a windows procedure. Malware may possibly utilize this memory location in part of an attack chain that includes writing code to shared sections of the process’s memory, placing a pointer to the code in EWM, then invoking execution by returning execution control to the address in the process’s EWM.\n\nExecution granted through EWM injection may allow access to both the target process's memory and possibly elevated privileges. Writing payloads to shared sections also avoids the use of highly monitored API calls such as <code>WriteProcessMemory</code> and <code>CreateRemoteThread</code>.(Citation: Elastic Process Injection July 2017) More sophisticated malware samples may also potentially bypass protection mechanisms such as data execution prevention (DEP) by triggering a combination of windows procedures and other system functions that will rewrite the malicious payload inside an executable portion of the target process.  (Citation: MalwareTech Power Loader Aug 2013) (Citation: WeLiveSecurity Gapz and Redyms Mar 2013)\n\nRunning code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via EWM injection may also evade detection from security products since the execution is masked under a legitimate process. ",
    "external_references": [
      {
        "source_name": "mitre-attack",
        "external_id": "T1055.011",
        "url": "https://attack.mitre.org/techniques/T1055/011"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633574.aspx",
        "description": "Microsoft. (n.d.). About Window Classes. Retrieved December 16, 2017.",
        "source_name": "Microsoft Window Classes"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633584.aspx",
        "description": "Microsoft. (n.d.). GetWindowLong function. Retrieved December 16, 2017.",
        "source_name": "Microsoft GetWindowLong function"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633591.aspx",
        "description": "Microsoft. (n.d.). SetWindowLong function. Retrieved December 16, 2017.",
        "source_name": "Microsoft SetWindowLong function"
      },
      {
        "url": "https://www.endgame.com/blog/technical-blog/ten-process-injection-techniques-technical-survey-common-and-trending-process",
        "description": "Hosseini, A. (2017, July 18). Ten Process Injection Techniques: A Technical Survey Of Common And Trending Process Injection Techniques. Retrieved December 7, 2017.",
        "source_name": "Elastic Process Injection July 2017"
      },
      {
        "url": "https://www.malwaretech.com/2013/08/powerloader-injection-something-truly.html",
        "description": "MalwareTech. (2013, August 13). PowerLoader Injection – Something truly amazing. Retrieved December 16, 2017.",
        "source_name": "MalwareTech Power Loader Aug 2013"
      },
      {
        "url": "https://www.welivesecurity.com/2013/03/19/gapz-and-redyms-droppers-based-on-power-loader-code/",
        "description": "Matrosov, A. (2013, March 19). Gapz and Redyms droppers based on Power Loader code. Retrieved December 16, 2017.",
        "source_name": "WeLiveSecurity Gapz and Redyms Mar 2013"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms644953.aspx",
        "description": "Microsoft. (n.d.). SendNotifyMessage function. Retrieved December 16, 2017.",
        "source_name": "Microsoft SendNotifyMessage function"
      }
    ],
    "id": "attack-pattern--0042a9f5-f053-4769-b3ef-9ad018dfa298",
    "kill_chain_phases": [
      {
        "kill_chain_name": "mitre-attack",
        "phase_name": "defense-evasion"
      },
      {
        "kill_chain_name": "mitre-attack",
        "phase_name": "privilege-escalation"
      }
    ],
    "modified": "2022-04-25T14:00:00.188Z",
    "name": "Extra Window Memory Injection",
    "object_marking_refs": [
      "marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168"
    ],
    "spec_version": "2.1",
    "type": "attack-pattern",
    "x_mitre_attack_spec_version": "2.1.0",
    "x_mitre_data_sources": [
      "Process: OS API Execution"
    ],
    "x_mitre_defense_bypassed": [
      "Anti-virus",
      "Application control"
    ],
    "x_mitre_detection": "Monitor for API calls related to enumerating and manipulating EWM such as GetWindowLong (Citation: Microsoft GetWindowLong function) and SetWindowLong (Citation: Microsoft SetWindowLong function). Malware associated with this technique have also used SendNotifyMessage (Citation: Microsoft SendNotifyMessage function) to trigger the associated window procedure and eventual malicious injection. (Citation: Elastic Process Injection July 2017)",
    "x_mitre_domains": [
      "enterprise-attack"
    ],
    "x_mitre_is_subtechnique": true,
    "x_mitre_modified_by_ref": "identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5",
    "x_mitre_platforms": [
      "Windows"
    ],
    "x_mitre_version": "1.0"
  },
  {
    "created": "2020-01-14T17:18:32.126Z",
    "created_by_ref": "identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5",
    "description": "Adversaries may inject malicious code into process via Extra Window Memory (EWM) in order to evade process-based defenses as well as possibly elevate privileges. EWM injection is a method of executing arbitrary code in the address space of a separate live process. \n\nBefore creating a window, graphical Windows-based processes must prescribe to or register a windows class, which stipulate appearance and behavior (via windows procedures, which are functions that handle input/output of data).(Citation: Microsoft Window Classes) Registration of new windows classes can include a request for up to 40 bytes of EWM to be appended to the allocated memory of each instance of that class. This EWM is intended to store data specific to that window and has specific application programming interface (API) functions to set and get its value. (Citation: Microsoft GetWindowLong function) (Citation: Microsoft SetWindowLong function)\n\nAlthough small, the EWM is large enough to store a 32-bit pointer and is often used to point to a windows procedure. Malware may possibly utilize this memory location in part of an attack chain that includes writing code to shared sections of the process’s memory, placing a pointer to the code in EWM, then invoking execution by returning execution control to the address in the process’s EWM.\n\nExecution granted through EWM injection may allow access to both the target process's memory and possibly elevated privileges. Writing payloads to shared sections also avoids the use of highly monitored API calls such as <code>WriteProcessMemory</code> and <code>CreateRemoteThread</code>.(Citation: Elastic Process Injection July 2017) More sophisticated malware samples may also potentially bypass protection mechanisms such as data execution prevention (DEP) by triggering a combination of windows procedures and other system functions that will rewrite the malicious payload inside an executable portion of the target process.  (Citation: MalwareTech Power Loader Aug 2013) (Citation: WeLiveSecurity Gapz and Redyms Mar 2013)\n\nRunning code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via EWM injection may also evade detection from security products since the execution is masked under a legitimate process. ",
    "external_references": [
      {
        "source_name": "mitre-attack",
        "external_id": "T1055.011",
        "url": "https://attack.mitre.org/techniques/T1055/011"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633574.aspx",
        "description": "Microsoft. (n.d.). About Window Classes. Retrieved December 16, 2017.",
        "source_name": "Microsoft Window Classes"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633584.aspx",
        "description": "Microsoft. (n.d.). GetWindowLong function. Retrieved December 16, 2017.",
        "source_name": "Microsoft GetWindowLong function"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633591.aspx",
        "description": "Microsoft. (n.d.). SetWindowLong function. Retrieved December 16, 2017.",
        "source_name": "Microsoft SetWindowLong function"
      },
      {
        "url": "https://www.endgame.com/blog/technical-blog/ten-process-injection-techniques-technical-survey-common-and-trending-process",
        "description": "Hosseini, A. (2017, July 18). Ten Process Injection Techniques: A Technical Survey Of Common And Trending Process Injection Techniques. Retrieved December 7, 2017.",
        "source_name": "Elastic Process Injection July 2017"
      },
      {
        "url": "https://www.malwaretech.com/2013/08/powerloader-injection-something-truly.html",
        "description": "MalwareTech. (2013, August 13). PowerLoader Injection – Something truly amazing. Retrieved December 16, 2017.",
        "source_name": "MalwareTech Power Loader Aug 2013"
      },
      {
        "url": "https://www.welivesecurity.com/2013/03/19/gapz-and-redyms-droppers-based-on-power-loader-code/",
        "description": "Matrosov, A. (2013, March 19). Gapz and Redyms droppers based on Power Loader code. Retrieved December 16, 2017.",
        "source_name": "WeLiveSecurity Gapz and Redyms Mar 2013"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms644953.aspx",
        "description": "Microsoft. (n.d.). SendNotifyMessage function. Retrieved December 16, 2017.",
        "source_name": "Microsoft SendNotifyMessage function"
      }
    ],
    "id": "attack-pattern--0042a9f5-f053-4769-b3ef-9ad018dfa298",
    "kill_chain_phases": [
      {
        "kill_chain_name": "mitre-attack",
        "phase_name": "defense-evasion"
      },
      {
        "kill_chain_name": "mitre-attack",
        "phase_name": "privilege-escalation"
      }
    ],
    "modified": "2022-04-25T14:00:00.188Z",
    "name": "Extra Window Memory Injection",
    "object_marking_refs": [
      "marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168"
    ],
    "spec_version": "2.1",
    "type": "attack-pattern",
    "x_mitre_attack_spec_version": "2.1.0",
    "x_mitre_data_sources": [
      "Process: OS API Execution"
    ],
    "x_mitre_defense_bypassed": [
      "Anti-virus",
      "Application control"
    ],
    "x_mitre_detection": "Monitor for API calls related to enumerating and manipulating EWM such as GetWindowLong (Citation: Microsoft GetWindowLong function) and SetWindowLong (Citation: Microsoft SetWindowLong function). Malware associated with this technique have also used SendNotifyMessage (Citation: Microsoft SendNotifyMessage function) to trigger the associated window procedure and eventual malicious injection. (Citation: Elastic Process Injection July 2017)",
    "x_mitre_domains": [
      "enterprise-attack"
    ],
    "x_mitre_is_subtechnique": true,
    "x_mitre_modified_by_ref": "identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5",
    "x_mitre_platforms": [
      "Windows"
    ],
    "x_mitre_version": "1.0"
  },
  {
    "created": "2020-01-14T17:18:32.126Z",
    "created_by_ref": "identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5",
    "description": "Adversaries may inject malicious code into process via Extra Window Memory (EWM) in order to evade process-based defenses as well as possibly elevate privileges. EWM injection is a method of executing arbitrary code in the address space of a separate live process. \n\nBefore creating a window, graphical Windows-based processes must prescribe to or register a windows class, which stipulate appearance and behavior (via windows procedures, which are functions that handle input/output of data).(Citation: Microsoft Window Classes) Registration of new windows classes can include a request for up to 40 bytes of EWM to be appended to the allocated memory of each instance of that class. This EWM is intended to store data specific to that window and has specific application programming interface (API) functions to set and get its value. (Citation: Microsoft GetWindowLong function) (Citation: Microsoft SetWindowLong function)\n\nAlthough small, the EWM is large enough to store a 32-bit pointer and is often used to point to a windows procedure. Malware may possibly utilize this memory location in part of an attack chain that includes writing code to shared sections of the process’s memory, placing a pointer to the code in EWM, then invoking execution by returning execution control to the address in the process’s EWM.\n\nExecution granted through EWM injection may allow access to both the target process's memory and possibly elevated privileges. Writing payloads to shared sections also avoids the use of highly monitored API calls such as <code>WriteProcessMemory</code> and <code>CreateRemoteThread</code>.(Citation: Elastic Process Injection July 2017) More sophisticated malware samples may also potentially bypass protection mechanisms such as data execution prevention (DEP) by triggering a combination of windows procedures and other system functions that will rewrite the malicious payload inside an executable portion of the target process.  (Citation: MalwareTech Power Loader Aug 2013) (Citation: WeLiveSecurity Gapz and Redyms Mar 2013)\n\nRunning code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via EWM injection may also evade detection from security products since the execution is masked under a legitimate process. ",
    "external_references": [
      {
        "source_name": "mitre-attack",
        "external_id": "T1055.011",
        "url": "https://attack.mitre.org/techniques/T1055/011"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633574.aspx",
        "description": "Microsoft. (n.d.). About Window Classes. Retrieved December 16, 2017.",
        "source_name": "Microsoft Window Classes"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633584.aspx",
        "description": "Microsoft. (n.d.). GetWindowLong function. Retrieved December 16, 2017.",
        "source_name": "Microsoft GetWindowLong function"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633591.aspx",
        "description": "Microsoft. (n.d.). SetWindowLong function. Retrieved December 16, 2017.",
        "source_name": "Microsoft SetWindowLong function"
      },
      {
        "url": "https://www.endgame.com/blog/technical-blog/ten-process-injection-techniques-technical-survey-common-and-trending-process",
        "description": "Hosseini, A. (2017, July 18). Ten Process Injection Techniques: A Technical Survey Of Common And Trending Process Injection Techniques. Retrieved December 7, 2017.",
        "source_name": "Elastic Process Injection July 2017"
      },
      {
        "url": "https://www.malwaretech.com/2013/08/powerloader-injection-something-truly.html",
        "description": "MalwareTech. (2013, August 13). PowerLoader Injection – Something truly amazing. Retrieved December 16, 2017.",
        "source_name": "MalwareTech Power Loader Aug 2013"
      },
      {
        "url": "https://www.welivesecurity.com/2013/03/19/gapz-and-redyms-droppers-based-on-power-loader-code/",
        "description": "Matrosov, A. (2013, March 19). Gapz and Redyms droppers based on Power Loader code. Retrieved December 16, 2017.",
        "source_name": "WeLiveSecurity Gapz and Redyms Mar 2013"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms644953.aspx",
        "description": "Microsoft. (n.d.). SendNotifyMessage function. Retrieved December 16, 2017.",
        "source_name": "Microsoft SendNotifyMessage function"
      }
    ],
    "id": "attack-pattern--0042a9f5-f053-4769-b3ef-9ad018dfa298",
    "kill_chain_phases": [
      {
        "kill_chain_name": "mitre-attack",
        "phase_name": "defense-evasion"
      },
      {
        "kill_chain_name": "mitre-attack",
        "phase_name": "privilege-escalation"
      }
    ],
    "modified": "2022-04-25T14:00:00.188Z",
    "name": "Extra Window Memory Injection",
    "object_marking_refs": [
      "marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168"
    ],
    "spec_version": "2.1",
    "type": "attack-pattern",
    "x_mitre_attack_spec_version": "2.1.0",
    "x_mitre_data_sources": [
      "Process: OS API Execution"
    ],
    "x_mitre_defense_bypassed": [
      "Anti-virus",
      "Application control"
    ],
    "x_mitre_detection": "Monitor for API calls related to enumerating and manipulating EWM such as GetWindowLong (Citation: Microsoft GetWindowLong function) and SetWindowLong (Citation: Microsoft SetWindowLong function). Malware associated with this technique have also used SendNotifyMessage (Citation: Microsoft SendNotifyMessage function) to trigger the associated window procedure and eventual malicious injection. (Citation: Elastic Process Injection July 2017)",
    "x_mitre_domains": [
      "enterprise-attack"
    ],
    "x_mitre_is_subtechnique": true,
    "x_mitre_modified_by_ref": "identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5",
    "x_mitre_platforms": [
      "Windows"
    ],
    "x_mitre_version": "1.0"
  },
  {
    "created": "2020-01-14T17:18:32.126Z",
    "created_by_ref": "identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5",
    "description": "Adversaries may inject malicious code into process via Extra Window Memory (EWM) in order to evade process-based defenses as well as possibly elevate privileges. EWM injection is a method of executing arbitrary code in the address space of a separate live process. \n\nBefore creating a window, graphical Windows-based processes must prescribe to or register a windows class, which stipulate appearance and behavior (via windows procedures, which are functions that handle input/output of data).(Citation: Microsoft Window Classes) Registration of new windows classes can include a request for up to 40 bytes of EWM to be appended to the allocated memory of each instance of that class. This EWM is intended to store data specific to that window and has specific application programming interface (API) functions to set and get its value. (Citation: Microsoft GetWindowLong function) (Citation: Microsoft SetWindowLong function)\n\nAlthough small, the EWM is large enough to store a 32-bit pointer and is often used to point to a windows procedure. Malware may possibly utilize this memory location in part of an attack chain that includes writing code to shared sections of the process’s memory, placing a pointer to the code in EWM, then invoking execution by returning execution control to the address in the process’s EWM.\n\nExecution granted through EWM injection may allow access to both the target process's memory and possibly elevated privileges. Writing payloads to shared sections also avoids the use of highly monitored API calls such as <code>WriteProcessMemory</code> and <code>CreateRemoteThread</code>.(Citation: Elastic Process Injection July 2017) More sophisticated malware samples may also potentially bypass protection mechanisms such as data execution prevention (DEP) by triggering a combination of windows procedures and other system functions that will rewrite the malicious payload inside an executable portion of the target process.  (Citation: MalwareTech Power Loader Aug 2013) (Citation: WeLiveSecurity Gapz and Redyms Mar 2013)\n\nRunning code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via EWM injection may also evade detection from security products since the execution is masked under a legitimate process. ",
    "external_references": [
      {
        "source_name": "mitre-attack",
        "external_id": "T1055.011",
        "url": "https://attack.mitre.org/techniques/T1055/011"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633574.aspx",
        "description": "Microsoft. (n.d.). About Window Classes. Retrieved December 16, 2017.",
        "source_name": "Microsoft Window Classes"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633584.aspx",
        "description": "Microsoft. (n.d.). GetWindowLong function. Retrieved December 16, 2017.",
        "source_name": "Microsoft GetWindowLong function"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633591.aspx",
        "description": "Microsoft. (n.d.). SetWindowLong function. Retrieved December 16, 2017.",
        "source_name": "Microsoft SetWindowLong function"
      },
      {
        "url": "https://www.endgame.com/blog/technical-blog/ten-process-injection-techniques-technical-survey-common-and-trending-process",
        "description": "Hosseini, A. (2017, July 18). Ten Process Injection Techniques: A Technical Survey Of Common And Trending Process Injection Techniques. Retrieved December 7, 2017.",
        "source_name": "Elastic Process Injection July 2017"
      },
      {
        "url": "https://www.malwaretech.com/2013/08/powerloader-injection-something-truly.html",
        "description": "MalwareTech. (2013, August 13). PowerLoader Injection – Something truly amazing. Retrieved December 16, 2017.",
        "source_name": "MalwareTech Power Loader Aug 2013"
      },
      {
        "url": "https://www.welivesecurity.com/2013/03/19/gapz-and-redyms-droppers-based-on-power-loader-code/",
        "description": "Matrosov, A. (2013, March 19). Gapz and Redyms droppers based on Power Loader code. Retrieved December 16, 2017.",
        "source_name": "WeLiveSecurity Gapz and Redyms Mar 2013"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms644953.aspx",
        "description": "Microsoft. (n.d.). SendNotifyMessage function. Retrieved December 16, 2017.",
        "source_name": "Microsoft SendNotifyMessage function"
      }
    ],
    "id": "attack-pattern--0042a9f5-f053-4769-b3ef-9ad018dfa298",
    "kill_chain_phases": [
      {
        "kill_chain_name": "mitre-attack",
        "phase_name": "defense-evasion"
      },
      {
        "kill_chain_name": "mitre-attack",
        "phase_name": "privilege-escalation"
      }
    ],
    "modified": "2022-04-25T14:00:00.188Z",
    "name": "Extra Window Memory Injection",
    "object_marking_refs": [
      "marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168"
    ],
    "spec_version": "2.1",
    "type": "attack-pattern",
    "x_mitre_attack_spec_version": "2.1.0",
    "x_mitre_data_sources": [
      "Process: OS API Execution"
    ],
    "x_mitre_defense_bypassed": [
      "Anti-virus",
      "Application control"
    ],
    "x_mitre_detection": "Monitor for API calls related to enumerating and manipulating EWM such as GetWindowLong (Citation: Microsoft GetWindowLong function) and SetWindowLong (Citation: Microsoft SetWindowLong function). Malware associated with this technique have also used SendNotifyMessage (Citation: Microsoft SendNotifyMessage function) to trigger the associated window procedure and eventual malicious injection. (Citation: Elastic Process Injection July 2017)",
    "x_mitre_domains": [
      "enterprise-attack"
    ],
    "x_mitre_is_subtechnique": true,
    "x_mitre_modified_by_ref": "identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5",
    "x_mitre_platforms": [
      "Windows"
    ],
    "x_mitre_version": "1.0"
  },
  {
    "created": "2020-01-14T17:18:32.126Z",
    "created_by_ref": "identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5",
    "description": "Adversaries may inject malicious code into process via Extra Window Memory (EWM) in order to evade process-based defenses as well as possibly elevate privileges. EWM injection is a method of executing arbitrary code in the address space of a separate live process. \n\nBefore creating a window, graphical Windows-based processes must prescribe to or register a windows class, which stipulate appearance and behavior (via windows procedures, which are functions that handle input/output of data).(Citation: Microsoft Window Classes) Registration of new windows classes can include a request for up to 40 bytes of EWM to be appended to the allocated memory of each instance of that class. This EWM is intended to store data specific to that window and has specific application programming interface (API) functions to set and get its value. (Citation: Microsoft GetWindowLong function) (Citation: Microsoft SetWindowLong function)\n\nAlthough small, the EWM is large enough to store a 32-bit pointer and is often used to point to a windows procedure. Malware may possibly utilize this memory location in part of an attack chain that includes writing code to shared sections of the process’s memory, placing a pointer to the code in EWM, then invoking execution by returning execution control to the address in the process’s EWM.\n\nExecution granted through EWM injection may allow access to both the target process's memory and possibly elevated privileges. Writing payloads to shared sections also avoids the use of highly monitored API calls such as <code>WriteProcessMemory</code> and <code>CreateRemoteThread</code>.(Citation: Elastic Process Injection July 2017) More sophisticated malware samples may also potentially bypass protection mechanisms such as data execution prevention (DEP) by triggering a combination of windows procedures and other system functions that will rewrite the malicious payload inside an executable portion of the target process.  (Citation: MalwareTech Power Loader Aug 2013) (Citation: WeLiveSecurity Gapz and Redyms Mar 2013)\n\nRunning code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via EWM injection may also evade detection from security products since the execution is masked under a legitimate process. ",
    "external_references": [
      {
        "source_name": "mitre-attack",
        "external_id": "T1055.011",
        "url": "https://attack.mitre.org/techniques/T1055/011"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633574.aspx",
        "description": "Microsoft. (n.d.). About Window Classes. Retrieved December 16, 2017.",
        "source_name": "Microsoft Window Classes"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633584.aspx",
        "description": "Microsoft. (n.d.). GetWindowLong function. Retrieved December 16, 2017.",
        "source_name": "Microsoft GetWindowLong function"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633591.aspx",
        "description": "Microsoft. (n.d.). SetWindowLong function. Retrieved December 16, 2017.",
        "source_name": "Microsoft SetWindowLong function"
      },
      {
        "url": "https://www.endgame.com/blog/technical-blog/ten-process-injection-techniques-technical-survey-common-and-trending-process",
        "description": "Hosseini, A. (2017, July 18). Ten Process Injection Techniques: A Technical Survey Of Common And Trending Process Injection Techniques. Retrieved December 7, 2017.",
        "source_name": "Elastic Process Injection July 2017"
      },
      {
        "url": "https://www.malwaretech.com/2013/08/powerloader-injection-something-truly.html",
        "description": "MalwareTech. (2013, August 13). PowerLoader Injection – Something truly amazing. Retrieved December 16, 2017.",
        "source_name": "MalwareTech Power Loader Aug 2013"
      },
      {
        "url": "https://www.welivesecurity.com/2013/03/19/gapz-and-redyms-droppers-based-on-power-loader-code/",
        "description": "Matrosov, A. (2013, March 19). Gapz and Redyms droppers based on Power Loader code. Retrieved December 16, 2017.",
        "source_name": "WeLiveSecurity Gapz and Redyms Mar 2013"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms644953.aspx",
        "description": "Microsoft. (n.d.). SendNotifyMessage function. Retrieved December 16, 2017.",
        "source_name": "Microsoft SendNotifyMessage function"
      }
    ],
    "id": "attack-pattern--0042a9f5-f053-4769-b3ef-9ad018dfa298",
    "kill_chain_phases": [
      {
        "kill_chain_name": "mitre-attack",
        "phase_name": "defense-evasion"
      },
      {
        "kill_chain_name": "mitre-attack",
        "phase_name": "privilege-escalation"
      }
    ],
    "modified": "2022-04-25T14:00:00.188Z",
    "name": "Extra Window Memory Injection",
    "object_marking_refs": [
      "marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168"
    ],
    "spec_version": "2.1",
    "type": "attack-pattern",
    "x_mitre_attack_spec_version": "2.1.0",
    "x_mitre_data_sources": [
      "Process: OS API Execution"
    ],
    "x_mitre_defense_bypassed": [
      "Anti-virus",
      "Application control"
    ],
    "x_mitre_detection": "Monitor for API calls related to enumerating and manipulating EWM such as GetWindowLong (Citation: Microsoft GetWindowLong function) and SetWindowLong (Citation: Microsoft SetWindowLong function). Malware associated with this technique have also used SendNotifyMessage (Citation: Microsoft SendNotifyMessage function) to trigger the associated window procedure and eventual malicious injection. (Citation: Elastic Process Injection July 2017)",
    "x_mitre_domains": [
      "enterprise-attack"
    ],
    "x_mitre_is_subtechnique": true,
    "x_mitre_modified_by_ref": "identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5",
    "x_mitre_platforms": [
      "Windows"
    ],
    "x_mitre_version": "1.0"
  },
  {
    "created": "2020-01-14T17:18:32.126Z",
    "created_by_ref": "identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5",
    "description": "Adversaries may inject malicious code into process via Extra Window Memory (EWM) in order to evade process-based defenses as well as possibly elevate privileges. EWM injection is a method of executing arbitrary code in the address space of a separate live process. \n\nBefore creating a window, graphical Windows-based processes must prescribe to or register a windows class, which stipulate appearance and behavior (via windows procedures, which are functions that handle input/output of data).(Citation: Microsoft Window Classes) Registration of new windows classes can include a request for up to 40 bytes of EWM to be appended to the allocated memory of each instance of that class. This EWM is intended to store data specific to that window and has specific application programming interface (API) functions to set and get its value. (Citation: Microsoft GetWindowLong function) (Citation: Microsoft SetWindowLong function)\n\nAlthough small, the EWM is large enough to store a 32-bit pointer and is often used to point to a windows procedure. Malware may possibly utilize this memory location in part of an attack chain that includes writing code to shared sections of the process’s memory, placing a pointer to the code in EWM, then invoking execution by returning execution control to the address in the process’s EWM.\n\nExecution granted through EWM injection may allow access to both the target process's memory and possibly elevated privileges. Writing payloads to shared sections also avoids the use of highly monitored API calls such as <code>WriteProcessMemory</code> and <code>CreateRemoteThread</code>.(Citation: Elastic Process Injection July 2017) More sophisticated malware samples may also potentially bypass protection mechanisms such as data execution prevention (DEP) by triggering a combination of windows procedures and other system functions that will rewrite the malicious payload inside an executable portion of the target process.  (Citation: MalwareTech Power Loader Aug 2013) (Citation: WeLiveSecurity Gapz and Redyms Mar 2013)\n\nRunning code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via EWM injection may also evade detection from security products since the execution is masked under a legitimate process. ",
    "external_references": [
      {
        "source_name": "mitre-attack",
        "external_id": "T1055.011",
        "url": "https://attack.mitre.org/techniques/T1055/011"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633574.aspx",
        "description": "Microsoft. (n.d.). About Window Classes. Retrieved December 16, 2017.",
        "source_name": "Microsoft Window Classes"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633584.aspx",
        "description": "Microsoft. (n.d.). GetWindowLong function. Retrieved December 16, 2017.",
        "source_name": "Microsoft GetWindowLong function"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633591.aspx",
        "description": "Microsoft. (n.d.). SetWindowLong function. Retrieved December 16, 2017.",
        "source_name": "Microsoft SetWindowLong function"
      },
      {
        "url": "https://www.endgame.com/blog/technical-blog/ten-process-injection-techniques-technical-survey-common-and-trending-process",
        "description": "Hosseini, A. (2017, July 18). Ten Process Injection Techniques: A Technical Survey Of Common And Trending Process Injection Techniques. Retrieved December 7, 2017.",
        "source_name": "Elastic Process Injection July 2017"
      },
      {
        "url": "https://www.malwaretech.com/2013/08/powerloader-injection-something-truly.html",
        "description": "MalwareTech. (2013, August 13). PowerLoader Injection – Something truly amazing. Retrieved December 16, 2017.",
        "source_name": "MalwareTech Power Loader Aug 2013"
      },
      {
        "url": "https://www.welivesecurity.com/2013/03/19/gapz-and-redyms-droppers-based-on-power-loader-code/",
        "description": "Matrosov, A. (2013, March 19). Gapz and Redyms droppers based on Power Loader code. Retrieved December 16, 2017.",
        "source_name": "WeLiveSecurity Gapz and Redyms Mar 2013"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms644953.aspx",
        "description": "Microsoft. (n.d.). SendNotifyMessage function. Retrieved December 16, 2017.",
        "source_name": "Microsoft SendNotifyMessage function"
      }
    ],
    "id": "attack-pattern--0042a9f5-f053-4769-b3ef-9ad018dfa298",
    "kill_chain_phases": [
      {
        "kill_chain_name": "mitre-attack",
        "phase_name": "defense-evasion"
      },
      {
        "kill_chain_name": "mitre-attack",
        "phase_name": "privilege-escalation"
      }
    ],
    "modified": "2022-04-25T14:00:00.188Z",
    "name": "Extra Window Memory Injection",
    "object_marking_refs": [
      "marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168"
    ],
    "spec_version": "2.1",
    "type": "attack-pattern",
    "x_mitre_attack_spec_version": "2.1.0",
    "x_mitre_data_sources": [
      "Process: OS API Execution"
    ],
    "x_mitre_defense_bypassed": [
      "Anti-virus",
      "Application control"
    ],
    "x_mitre_detection": "Monitor for API calls related to enumerating and manipulating EWM such as GetWindowLong (Citation: Microsoft GetWindowLong function) and SetWindowLong (Citation: Microsoft SetWindowLong function). Malware associated with this technique have also used SendNotifyMessage (Citation: Microsoft SendNotifyMessage function) to trigger the associated window procedure and eventual malicious injection. (Citation: Elastic Process Injection July 2017)",
    "x_mitre_domains": [
      "enterprise-attack"
    ],
    "x_mitre_is_subtechnique": true,
    "x_mitre_modified_by_ref": "identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5",
    "x_mitre_platforms": [
      "Windows"
    ],
    "x_mitre_version": "1.0"
  },
  {
    "created": "2020-01-14T17:18:32.126Z",
    "created_by_ref": "identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5",
    "description": "Adversaries may inject malicious code into process via Extra Window Memory (EWM) in order to evade process-based defenses as well as possibly elevate privileges. EWM injection is a method of executing arbitrary code in the address space of a separate live process. \n\nBefore creating a window, graphical Windows-based processes must prescribe to or register a windows class, which stipulate appearance and behavior (via windows procedures, which are functions that handle input/output of data).(Citation: Microsoft Window Classes) Registration of new windows classes can include a request for up to 40 bytes of EWM to be appended to the allocated memory of each instance of that class. This EWM is intended to store data specific to that window and has specific application programming interface (API) functions to set and get its value. (Citation: Microsoft GetWindowLong function) (Citation: Microsoft SetWindowLong function)\n\nAlthough small, the EWM is large enough to store a 32-bit pointer and is often used to point to a windows procedure. Malware may possibly utilize this memory location in part of an attack chain that includes writing code to shared sections of the process’s memory, placing a pointer to the code in EWM, then invoking execution by returning execution control to the address in the process’s EWM.\n\nExecution granted through EWM injection may allow access to both the target process's memory and possibly elevated privileges. Writing payloads to shared sections also avoids the use of highly monitored API calls such as <code>WriteProcessMemory</code> and <code>CreateRemoteThread</code>.(Citation: Elastic Process Injection July 2017) More sophisticated malware samples may also potentially bypass protection mechanisms such as data execution prevention (DEP) by triggering a combination of windows procedures and other system functions that will rewrite the malicious payload inside an executable portion of the target process.  (Citation: MalwareTech Power Loader Aug 2013) (Citation: WeLiveSecurity Gapz and Redyms Mar 2013)\n\nRunning code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via EWM injection may also evade detection from security products since the execution is masked under a legitimate process. ",
    "external_references": [
      {
        "source_name": "mitre-attack",
        "external_id": "T1055.011",
        "url": "https://attack.mitre.org/techniques/T1055/011"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633574.aspx",
        "description": "Microsoft. (n.d.). About Window Classes. Retrieved December 16, 2017.",
        "source_name": "Microsoft Window Classes"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633584.aspx",
        "description": "Microsoft. (n.d.). GetWindowLong function. Retrieved December 16, 2017.",
        "source_name": "Microsoft GetWindowLong function"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633591.aspx",
        "description": "Microsoft. (n.d.). SetWindowLong function. Retrieved December 16, 2017.",
        "source_name": "Microsoft SetWindowLong function"
      },
      {
        "url": "https://www.endgame.com/blog/technical-blog/ten-process-injection-techniques-technical-survey-common-and-trending-process",
        "description": "Hosseini, A. (2017, July 18). Ten Process Injection Techniques: A Technical Survey Of Common And Trending Process Injection Techniques. Retrieved December 7, 2017.",
        "source_name": "Elastic Process Injection July 2017"
      },
      {
        "url": "https://www.malwaretech.com/2013/08/powerloader-injection-something-truly.html",
        "description": "MalwareTech. (2013, August 13). PowerLoader Injection – Something truly amazing. Retrieved December 16, 2017.",
        "source_name": "MalwareTech Power Loader Aug 2013"
      },
      {
        "url": "https://www.welivesecurity.com/2013/03/19/gapz-and-redyms-droppers-based-on-power-loader-code/",
        "description": "Matrosov, A. (2013, March 19). Gapz and Redyms droppers based on Power Loader code. Retrieved December 16, 2017.",
        "source_name": "WeLiveSecurity Gapz and Redyms Mar 2013"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms644953.aspx",
        "description": "Microsoft. (n.d.). SendNotifyMessage function. Retrieved December 16, 2017.",
        "source_name": "Microsoft SendNotifyMessage function"
      }
    ],
    "id": "attack-pattern--0042a9f5-f053-4769-b3ef-9ad018dfa298",
    "kill_chain_phases": [
      {
        "kill_chain_name": "mitre-attack",
        "phase_name": "defense-evasion"
      },
      {
        "kill_chain_name": "mitre-attack",
        "phase_name": "privilege-escalation"
      }
    ],
    "modified": "2022-04-25T14:00:00.188Z",
    "name": "Extra Window Memory Injection",
    "object_marking_refs": [
      "marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168"
    ],
    "spec_version": "2.1",
    "type": "attack-pattern",
    "x_mitre_attack_spec_version": "2.1.0",
    "x_mitre_data_sources": [
      "Process: OS API Execution"
    ],
    "x_mitre_defense_bypassed": [
      "Anti-virus",
      "Application control"
    ],
    "x_mitre_detection": "Monitor for API calls related to enumerating and manipulating EWM such as GetWindowLong (Citation: Microsoft GetWindowLong function) and SetWindowLong (Citation: Microsoft SetWindowLong function). Malware associated with this technique have also used SendNotifyMessage (Citation: Microsoft SendNotifyMessage function) to trigger the associated window procedure and eventual malicious injection. (Citation: Elastic Process Injection July 2017)",
    "x_mitre_domains": [
      "enterprise-attack"
    ],
    "x_mitre_is_subtechnique": true,
    "x_mitre_modified_by_ref": "identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5",
    "x_mitre_platforms": [
      "Windows"
    ],
    "x_mitre_version": "1.0"
  },
  {
    "created": "2020-01-14T17:18:32.126Z",
    "created_by_ref": "identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5",
    "description": "Adversaries may inject malicious code into process via Extra Window Memory (EWM) in order to evade process-based defenses as well as possibly elevate privileges. EWM injection is a method of executing arbitrary code in the address space of a separate live process. \n\nBefore creating a window, graphical Windows-based processes must prescribe to or register a windows class, which stipulate appearance and behavior (via windows procedures, which are functions that handle input/output of data).(Citation: Microsoft Window Classes) Registration of new windows classes can include a request for up to 40 bytes of EWM to be appended to the allocated memory of each instance of that class. This EWM is intended to store data specific to that window and has specific application programming interface (API) functions to set and get its value. (Citation: Microsoft GetWindowLong function) (Citation: Microsoft SetWindowLong function)\n\nAlthough small, the EWM is large enough to store a 32-bit pointer and is often used to point to a windows procedure. Malware may possibly utilize this memory location in part of an attack chain that includes writing code to shared sections of the process’s memory, placing a pointer to the code in EWM, then invoking execution by returning execution control to the address in the process’s EWM.\n\nExecution granted through EWM injection may allow access to both the target process's memory and possibly elevated privileges. Writing payloads to shared sections also avoids the use of highly monitored API calls such as <code>WriteProcessMemory</code> and <code>CreateRemoteThread</code>.(Citation: Elastic Process Injection July 2017) More sophisticated malware samples may also potentially bypass protection mechanisms such as data execution prevention (DEP) by triggering a combination of windows procedures and other system functions that will rewrite the malicious payload inside an executable portion of the target process.  (Citation: MalwareTech Power Loader Aug 2013) (Citation: WeLiveSecurity Gapz and Redyms Mar 2013)\n\nRunning code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via EWM injection may also evade detection from security products since the execution is masked under a legitimate process. ",
    "external_references": [
      {
        "source_name": "mitre-attack",
        "external_id": "T1055.011",
        "url": "https://attack.mitre.org/techniques/T1055/011"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633574.aspx",
        "description": "Microsoft. (n.d.). About Window Classes. Retrieved December 16, 2017.",
        "source_name": "Microsoft Window Classes"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633584.aspx",
        "description": "Microsoft. (n.d.). GetWindowLong function. Retrieved December 16, 2017.",
        "source_name": "Microsoft GetWindowLong function"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633591.aspx",
        "description": "Microsoft. (n.d.). SetWindowLong function. Retrieved December 16, 2017.",
        "source_name": "Microsoft SetWindowLong function"
      },
      {
        "url": "https://www.endgame.com/blog/technical-blog/ten-process-injection-techniques-technical-survey-common-and-trending-process",
        "description": "Hosseini, A. (2017, July 18). Ten Process Injection Techniques: A Technical Survey Of Common And Trending Process Injection Techniques. Retrieved December 7, 2017.",
        "source_name": "Elastic Process Injection July 2017"
      },
      {
        "url": "https://www.malwaretech.com/2013/08/powerloader-injection-something-truly.html",
        "description": "MalwareTech. (2013, August 13). PowerLoader Injection – Something truly amazing. Retrieved December 16, 2017.",
        "source_name": "MalwareTech Power Loader Aug 2013"
      },
      {
        "url": "https://www.welivesecurity.com/2013/03/19/gapz-and-redyms-droppers-based-on-power-loader-code/",
        "description": "Matrosov, A. (2013, March 19). Gapz and Redyms droppers based on Power Loader code. Retrieved December 16, 2017.",
        "source_name": "WeLiveSecurity Gapz and Redyms Mar 2013"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms644953.aspx",
        "description": "Microsoft. (n.d.). SendNotifyMessage function. Retrieved December 16, 2017.",
        "source_name": "Microsoft SendNotifyMessage function"
      }
    ],
    "id": "attack-pattern--0042a9f5-f053-4769-b3ef-9ad018dfa298",
    "kill_chain_phases": [
      {
        "kill_chain_name": "mitre-attack",
        "phase_name": "defense-evasion"
      },
      {
        "kill_chain_name": "mitre-attack",
        "phase_name": "privilege-escalation"
      }
    ],
    "modified": "2022-04-25T14:00:00.188Z",
    "name": "Extra Window Memory Injection",
    "object_marking_refs": [
      "marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168"
    ],
    "spec_version": "2.1",
    "type": "attack-pattern",
    "x_mitre_attack_spec_version": "2.1.0",
    "x_mitre_data_sources": [
      "Process: OS API Execution"
    ],
    "x_mitre_defense_bypassed": [
      "Anti-virus",
      "Application control"
    ],
    "x_mitre_detection": "Monitor for API calls related to enumerating and manipulating EWM such as GetWindowLong (Citation: Microsoft GetWindowLong function) and SetWindowLong (Citation: Microsoft SetWindowLong function). Malware associated with this technique have also used SendNotifyMessage (Citation: Microsoft SendNotifyMessage function) to trigger the associated window procedure and eventual malicious injection. (Citation: Elastic Process Injection July 2017)",
    "x_mitre_domains": [
      "enterprise-attack"
    ],
    "x_mitre_is_subtechnique": true,
    "x_mitre_modified_by_ref": "identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5",
    "x_mitre_platforms": [
      "Windows"
    ],
    "x_mitre_version": "1.0"
  },
  {
    "created": "2020-01-14T17:18:32.126Z",
    "created_by_ref": "identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5",
    "description": "Adversaries may inject malicious code into process via Extra Window Memory (EWM) in order to evade process-based defenses as well as possibly elevate privileges. EWM injection is a method of executing arbitrary code in the address space of a separate live process. \n\nBefore creating a window, graphical Windows-based processes must prescribe to or register a windows class, which stipulate appearance and behavior (via windows procedures, which are functions that handle input/output of data).(Citation: Microsoft Window Classes) Registration of new windows classes can include a request for up to 40 bytes of EWM to be appended to the allocated memory of each instance of that class. This EWM is intended to store data specific to that window and has specific application programming interface (API) functions to set and get its value. (Citation: Microsoft GetWindowLong function) (Citation: Microsoft SetWindowLong function)\n\nAlthough small, the EWM is large enough to store a 32-bit pointer and is often used to point to a windows procedure. Malware may possibly utilize this memory location in part of an attack chain that includes writing code to shared sections of the process’s memory, placing a pointer to the code in EWM, then invoking execution by returning execution control to the address in the process’s EWM.\n\nExecution granted through EWM injection may allow access to both the target process's memory and possibly elevated privileges. Writing payloads to shared sections also avoids the use of highly monitored API calls such as <code>WriteProcessMemory</code> and <code>CreateRemoteThread</code>.(Citation: Elastic Process Injection July 2017) More sophisticated malware samples may also potentially bypass protection mechanisms such as data execution prevention (DEP) by triggering a combination of windows procedures and other system functions that will rewrite the malicious payload inside an executable portion of the target process.  (Citation: MalwareTech Power Loader Aug 2013) (Citation: WeLiveSecurity Gapz and Redyms Mar 2013)\n\nRunning code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via EWM injection may also evade detection from security products since the execution is masked under a legitimate process. ",
    "external_references": [
      {
        "source_name": "mitre-attack",
        "external_id": "T1055.011",
        "url": "https://attack.mitre.org/techniques/T1055/011"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633574.aspx",
        "description": "Microsoft. (n.d.). About Window Classes. Retrieved December 16, 2017.",
        "source_name": "Microsoft Window Classes"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633584.aspx",
        "description": "Microsoft. (n.d.). GetWindowLong function. Retrieved December 16, 2017.",
        "source_name": "Microsoft GetWindowLong function"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633591.aspx",
        "description": "Microsoft. (n.d.). SetWindowLong function. Retrieved December 16, 2017.",
        "source_name": "Microsoft SetWindowLong function"
      },
      {
        "url": "https://www.endgame.com/blog/technical-blog/ten-process-injection-techniques-technical-survey-common-and-trending-process",
        "description": "Hosseini, A. (2017, July 18). Ten Process Injection Techniques: A Technical Survey Of Common And Trending Process Injection Techniques. Retrieved December 7, 2017.",
        "source_name": "Elastic Process Injection July 2017"
      },
      {
        "url": "https://www.malwaretech.com/2013/08/powerloader-injection-something-truly.html",
        "description": "MalwareTech. (2013, August 13). PowerLoader Injection – Something truly amazing. Retrieved December 16, 2017.",
        "source_name": "MalwareTech Power Loader Aug 2013"
      },
      {
        "url": "https://www.welivesecurity.com/2013/03/19/gapz-and-redyms-droppers-based-on-power-loader-code/",
        "description": "Matrosov, A. (2013, March 19). Gapz and Redyms droppers based on Power Loader code. Retrieved December 16, 2017.",
        "source_name": "WeLiveSecurity Gapz and Redyms Mar 2013"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms644953.aspx",
        "description": "Microsoft. (n.d.). SendNotifyMessage function. Retrieved December 16, 2017.",
        "source_name": "Microsoft SendNotifyMessage function"
      }
    ],
    "id": "attack-pattern--0042a9f5-f053-4769-b3ef-9ad018dfa298",
    "kill_chain_phases": [
      {
        "kill_chain_name": "mitre-attack",
        "phase_name": "defense-evasion"
      },
      {
        "kill_chain_name": "mitre-attack",
        "phase_name": "privilege-escalation"
      }
    ],
    "modified": "2022-04-25T14:00:00.188Z",
    "name": "Extra Window Memory Injection",
    "object_marking_refs": [
      "marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168"
    ],
    "spec_version": "2.1",
    "type": "attack-pattern",
    "x_mitre_attack_spec_version": "2.1.0",
    "x_mitre_data_sources": [
      "Process: OS API Execution"
    ],
    "x_mitre_defense_bypassed": [
      "Anti-virus",
      "Application control"
    ],
    "x_mitre_detection": "Monitor for API calls related to enumerating and manipulating EWM such as GetWindowLong (Citation: Microsoft GetWindowLong function) and SetWindowLong (Citation: Microsoft SetWindowLong function). Malware associated with this technique have also used SendNotifyMessage (Citation: Microsoft SendNotifyMessage function) to trigger the associated window procedure and eventual malicious injection. (Citation: Elastic Process Injection July 2017)",
    "x_mitre_domains": [
      "enterprise-attack"
    ],
    "x_mitre_is_subtechnique": true,
    "x_mitre_modified_by_ref": "identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5",
    "x_mitre_platforms": [
      "Windows"
    ],
    "x_mitre_version": "1.0"
  },
  {
    "created": "2020-01-14T17:18:32.126Z",
    "created_by_ref": "identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5",
    "description": "Adversaries may inject malicious code into process via Extra Window Memory (EWM) in order to evade process-based defenses as well as possibly elevate privileges. EWM injection is a method of executing arbitrary code in the address space of a separate live process. \n\nBefore creating a window, graphical Windows-based processes must prescribe to or register a windows class, which stipulate appearance and behavior (via windows procedures, which are functions that handle input/output of data).(Citation: Microsoft Window Classes) Registration of new windows classes can include a request for up to 40 bytes of EWM to be appended to the allocated memory of each instance of that class. This EWM is intended to store data specific to that window and has specific application programming interface (API) functions to set and get its value. (Citation: Microsoft GetWindowLong function) (Citation: Microsoft SetWindowLong function)\n\nAlthough small, the EWM is large enough to store a 32-bit pointer and is often used to point to a windows procedure. Malware may possibly utilize this memory location in part of an attack chain that includes writing code to shared sections of the process’s memory, placing a pointer to the code in EWM, then invoking execution by returning execution control to the address in the process’s EWM.\n\nExecution granted through EWM injection may allow access to both the target process's memory and possibly elevated privileges. Writing payloads to shared sections also avoids the use of highly monitored API calls such as <code>WriteProcessMemory</code> and <code>CreateRemoteThread</code>.(Citation: Elastic Process Injection July 2017) More sophisticated malware samples may also potentially bypass protection mechanisms such as data execution prevention (DEP) by triggering a combination of windows procedures and other system functions that will rewrite the malicious payload inside an executable portion of the target process.  (Citation: MalwareTech Power Loader Aug 2013) (Citation: WeLiveSecurity Gapz and Redyms Mar 2013)\n\nRunning code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via EWM injection may also evade detection from security products since the execution is masked under a legitimate process. ",
    "external_references": [
      {
        "source_name": "mitre-attack",
        "external_id": "T1055.011",
        "url": "https://attack.mitre.org/techniques/T1055/011"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633574.aspx",
        "description": "Microsoft. (n.d.). About Window Classes. Retrieved December 16, 2017.",
        "source_name": "Microsoft Window Classes"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633584.aspx",
        "description": "Microsoft. (n.d.). GetWindowLong function. Retrieved December 16, 2017.",
        "source_name": "Microsoft GetWindowLong function"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633591.aspx",
        "description": "Microsoft. (n.d.). SetWindowLong function. Retrieved December 16, 2017.",
        "source_name": "Microsoft SetWindowLong function"
      },
      {
        "url": "https://www.endgame.com/blog/technical-blog/ten-process-injection-techniques-technical-survey-common-and-trending-process",
        "description": "Hosseini, A. (2017, July 18). Ten Process Injection Techniques: A Technical Survey Of Common And Trending Process Injection Techniques. Retrieved December 7, 2017.",
        "source_name": "Elastic Process Injection July 2017"
      },
      {
        "url": "https://www.malwaretech.com/2013/08/powerloader-injection-something-truly.html",
        "description": "MalwareTech. (2013, August 13). PowerLoader Injection – Something truly amazing. Retrieved December 16, 2017.",
        "source_name": "MalwareTech Power Loader Aug 2013"
      },
      {
        "url": "https://www.welivesecurity.com/2013/03/19/gapz-and-redyms-droppers-based-on-power-loader-code/",
        "description": "Matrosov, A. (2013, March 19). Gapz and Redyms droppers based on Power Loader code. Retrieved December 16, 2017.",
        "source_name": "WeLiveSecurity Gapz and Redyms Mar 2013"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms644953.aspx",
        "description": "Microsoft. (n.d.). SendNotifyMessage function. Retrieved December 16, 2017.",
        "source_name": "Microsoft SendNotifyMessage function"
      }
    ],
    "id": "attack-pattern--0042a9f5-f053-4769-b3ef-9ad018dfa298",
    "kill_chain_phases": [
      {
        "kill_chain_name": "mitre-attack",
        "phase_name": "defense-evasion"
      },
      {
        "kill_chain_name": "mitre-attack",
        "phase_name": "privilege-escalation"
      }
    ],
    "modified": "2022-04-25T14:00:00.188Z",
    "name": "Extra Window Memory Injection",
    "object_marking_refs": [
      "marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168"
    ],
    "spec_version": "2.1",
    "type": "attack-pattern",
    "x_mitre_attack_spec_version": "2.1.0",
    "x_mitre_contributors": [],
    "x_mitre_data_sources": [
      "Process: OS API Execution"
    ],
    "x_mitre_defense_bypassed": [
      "Anti-virus",
      "Application control"
    ],
    "x_mitre_detection": "Monitor for API calls related to enumerating and manipulating EWM such as GetWindowLong (Citation: Microsoft GetWindowLong function) and SetWindowLong (Citation: Microsoft SetWindowLong function). Malware associated with this technique have also used SendNotifyMessage (Citation: Microsoft SendNotifyMessage function) to trigger the associated window procedure and eventual malicious injection. (Citation: Elastic Process Injection July 2017)",
    "x_mitre_domains": [
      "enterprise-attack"
    ],
    "x_mitre_is_subtechnique": true,
    "x_mitre_modified_by_ref": "identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5",
    "x_mitre_platforms": [
      "Windows"
    ],
    "x_mitre_version": "1.0"
  },
  {
    "created": "2020-01-14T17:18:32.126Z",
    "created_by_ref": "identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5",
    "description": "Adversaries may inject malicious code into process via Extra Window Memory (EWM) in order to evade process-based defenses as well as possibly elevate privileges. EWM injection is a method of executing arbitrary code in the address space of a separate live process. \n\nBefore creating a window, graphical Windows-based processes must prescribe to or register a windows class, which stipulate appearance and behavior (via windows procedures, which are functions that handle input/output of data).(Citation: Microsoft Window Classes) Registration of new windows classes can include a request for up to 40 bytes of EWM to be appended to the allocated memory of each instance of that class. This EWM is intended to store data specific to that window and has specific application programming interface (API) functions to set and get its value. (Citation: Microsoft GetWindowLong function) (Citation: Microsoft SetWindowLong function)\n\nAlthough small, the EWM is large enough to store a 32-bit pointer and is often used to point to a windows procedure. Malware may possibly utilize this memory location in part of an attack chain that includes writing code to shared sections of the process’s memory, placing a pointer to the code in EWM, then invoking execution by returning execution control to the address in the process’s EWM.\n\nExecution granted through EWM injection may allow access to both the target process's memory and possibly elevated privileges. Writing payloads to shared sections also avoids the use of highly monitored API calls such as <code>WriteProcessMemory</code> and <code>CreateRemoteThread</code>.(Citation: Elastic Process Injection July 2017) More sophisticated malware samples may also potentially bypass protection mechanisms such as data execution prevention (DEP) by triggering a combination of windows procedures and other system functions that will rewrite the malicious payload inside an executable portion of the target process.  (Citation: MalwareTech Power Loader Aug 2013) (Citation: WeLiveSecurity Gapz and Redyms Mar 2013)\n\nRunning code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via EWM injection may also evade detection from security products since the execution is masked under a legitimate process. ",
    "external_references": [
      {
        "source_name": "mitre-attack",
        "external_id": "T1055.011",
        "url": "https://attack.mitre.org/techniques/T1055/011"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633574.aspx",
        "description": "Microsoft. (n.d.). About Window Classes. Retrieved December 16, 2017.",
        "source_name": "Microsoft Window Classes"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633584.aspx",
        "description": "Microsoft. (n.d.). GetWindowLong function. Retrieved December 16, 2017.",
        "source_name": "Microsoft GetWindowLong function"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633591.aspx",
        "description": "Microsoft. (n.d.). SetWindowLong function. Retrieved December 16, 2017.",
        "source_name": "Microsoft SetWindowLong function"
      },
      {
        "url": "https://www.endgame.com/blog/technical-blog/ten-process-injection-techniques-technical-survey-common-and-trending-process",
        "description": "Hosseini, A. (2017, July 18). Ten Process Injection Techniques: A Technical Survey Of Common And Trending Process Injection Techniques. Retrieved December 7, 2017.",
        "source_name": "Elastic Process Injection July 2017"
      },
      {
        "url": "https://www.malwaretech.com/2013/08/powerloader-injection-something-truly.html",
        "description": "MalwareTech. (2013, August 13). PowerLoader Injection – Something truly amazing. Retrieved December 16, 2017.",
        "source_name": "MalwareTech Power Loader Aug 2013"
      },
      {
        "url": "https://www.welivesecurity.com/2013/03/19/gapz-and-redyms-droppers-based-on-power-loader-code/",
        "description": "Matrosov, A. (2013, March 19). Gapz and Redyms droppers based on Power Loader code. Retrieved December 16, 2017.",
        "source_name": "WeLiveSecurity Gapz and Redyms Mar 2013"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms644953.aspx",
        "description": "Microsoft. (n.d.). SendNotifyMessage function. Retrieved December 16, 2017.",
        "source_name": "Microsoft SendNotifyMessage function"
      }
    ],
    "id": "attack-pattern--0042a9f5-f053-4769-b3ef-9ad018dfa298",
    "kill_chain_phases": [
      {
        "kill_chain_name": "mitre-attack",
        "phase_name": "defense-evasion"
      },
      {
        "kill_chain_name": "mitre-attack",
        "phase_name": "privilege-escalation"
      }
    ],
    "modified": "2022-04-25T14:00:00.188Z",
    "name": "Extra Window Memory Injection",
    "object_marking_refs": [
      "marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168"
    ],
    "spec_version": "2.1",
    "type": "attack-pattern",
    "x_mitre_attack_spec_version": "2.1.0",
    "x_mitre_data_sources": [
      "Process: OS API Execution"
    ],
    "x_mitre_defense_bypassed": [
      "Anti-virus",
      "Application control"
    ],
    "x_mitre_detection": "Monitor for API calls related to enumerating and manipulating EWM such as GetWindowLong (Citation: Microsoft GetWindowLong function) and SetWindowLong (Citation: Microsoft SetWindowLong function). Malware associated with this technique have also used SendNotifyMessage (Citation: Microsoft SendNotifyMessage function) to trigger the associated window procedure and eventual malicious injection. (Citation: Elastic Process Injection July 2017)",
    "x_mitre_domains": [
      "enterprise-attack"
    ],
    "x_mitre_is_subtechnique": true,
    "x_mitre_modified_by_ref": "identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5",
    "x_mitre_platforms": [
      "Windows"
    ],
    "x_mitre_version": "1.0"
  },
  {
    "created": "2020-01-14T17:18:32.126Z",
    "created_by_ref": "identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5",
    "description": "Adversaries may inject malicious code into process via Extra Window Memory (EWM) in order to evade process-based defenses as well as possibly elevate privileges. EWM injection is a method of executing arbitrary code in the address space of a separate live process. \n\nBefore creating a window, graphical Windows-based processes must prescribe to or register a windows class, which stipulate appearance and behavior (via windows procedures, which are functions that handle input/output of data).(Citation: Microsoft Window Classes) Registration of new windows classes can include a request for up to 40 bytes of EWM to be appended to the allocated memory of each instance of that class. This EWM is intended to store data specific to that window and has specific application programming interface (API) functions to set and get its value. (Citation: Microsoft GetWindowLong function) (Citation: Microsoft SetWindowLong function)\n\nAlthough small, the EWM is large enough to store a 32-bit pointer and is often used to point to a windows procedure. Malware may possibly utilize this memory location in part of an attack chain that includes writing code to shared sections of the process’s memory, placing a pointer to the code in EWM, then invoking execution by returning execution control to the address in the process’s EWM.\n\nExecution granted through EWM injection may allow access to both the target process's memory and possibly elevated privileges. Writing payloads to shared sections also avoids the use of highly monitored API calls such as <code>WriteProcessMemory</code> and <code>CreateRemoteThread</code>.(Citation: Elastic Process Injection July 2017) More sophisticated malware samples may also potentially bypass protection mechanisms such as data execution prevention (DEP) by triggering a combination of windows procedures and other system functions that will rewrite the malicious payload inside an executable portion of the target process.  (Citation: MalwareTech Power Loader Aug 2013) (Citation: WeLiveSecurity Gapz and Redyms Mar 2013)\n\nRunning code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via EWM injection may also evade detection from security products since the execution is masked under a legitimate process. ",
    "external_references": [
      {
        "source_name": "mitre-attack",
        "external_id": "T1055.011",
        "url": "https://attack.mitre.org/techniques/T1055/011"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633574.aspx",
        "description": "Microsoft. (n.d.). About Window Classes. Retrieved December 16, 2017.",
        "source_name": "Microsoft Window Classes"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633584.aspx",
        "description": "Microsoft. (n.d.). GetWindowLong function. Retrieved December 16, 2017.",
        "source_name": "Microsoft GetWindowLong function"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633591.aspx",
        "description": "Microsoft. (n.d.). SetWindowLong function. Retrieved December 16, 2017.",
        "source_name": "Microsoft SetWindowLong function"
      },
      {
        "url": "https://www.endgame.com/blog/technical-blog/ten-process-injection-techniques-technical-survey-common-and-trending-process",
        "description": "Hosseini, A. (2017, July 18). Ten Process Injection Techniques: A Technical Survey Of Common And Trending Process Injection Techniques. Retrieved December 7, 2017.",
        "source_name": "Elastic Process Injection July 2017"
      },
      {
        "url": "https://www.malwaretech.com/2013/08/powerloader-injection-something-truly.html",
        "description": "MalwareTech. (2013, August 13). PowerLoader Injection – Something truly amazing. Retrieved December 16, 2017.",
        "source_name": "MalwareTech Power Loader Aug 2013"
      },
      {
        "url": "https://www.welivesecurity.com/2013/03/19/gapz-and-redyms-droppers-based-on-power-loader-code/",
        "description": "Matrosov, A. (2013, March 19). Gapz and Redyms droppers based on Power Loader code. Retrieved December 16, 2017.",
        "source_name": "WeLiveSecurity Gapz and Redyms Mar 2013"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms644953.aspx",
        "description": "Microsoft. (n.d.). SendNotifyMessage function. Retrieved December 16, 2017.",
        "source_name": "Microsoft SendNotifyMessage function"
      }
    ],
    "id": "attack-pattern--0042a9f5-f053-4769-b3ef-9ad018dfa298",
    "kill_chain_phases": [
      {
        "kill_chain_name": "mitre-attack",
        "phase_name": "defense-evasion"
      },
      {
        "kill_chain_name": "mitre-attack",
        "phase_name": "privilege-escalation"
      }
    ],
    "modified": "2022-04-25T14:00:00.188Z",
    "name": "Extra Window Memory Injection",
    "object_marking_refs": [
      "marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168"
    ],
    "spec_version": "2.1",
    "type": "attack-pattern",
    "x_mitre_attack_spec_version": "2.1.0",
    "x_mitre_data_sources": [
      "Process: OS API Execution"
    ],
    "x_mitre_defense_bypassed": [
      "Anti-virus",
      "Application control"
    ],
    "x_mitre_detection": "Monitor for API calls related to enumerating and manipulating EWM such as GetWindowLong (Citation: Microsoft GetWindowLong function) and SetWindowLong (Citation: Microsoft SetWindowLong function). Malware associated with this technique have also used SendNotifyMessage (Citation: Microsoft SendNotifyMessage function) to trigger the associated window procedure and eventual malicious injection. (Citation: Elastic Process Injection July 2017)",
    "x_mitre_domains": [
      "enterprise-attack"
    ],
    "x_mitre_is_subtechnique": true,
    "x_mitre_modified_by_ref": "identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5",
    "x_mitre_platforms": [
      "Windows"
    ],
    "x_mitre_version": "1.0"
  },
  {
    "created": "2020-01-14T17:18:32.126Z",
    "created_by_ref": "identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5",
    "description": "Adversaries may inject malicious code into process via Extra Window Memory (EWM) in order to evade process-based defenses as well as possibly elevate privileges. EWM injection is a method of executing arbitrary code in the address space of a separate live process. \n\nBefore creating a window, graphical Windows-based processes must prescribe to or register a windows class, which stipulate appearance and behavior (via windows procedures, which are functions that handle input/output of data).(Citation: Microsoft Window Classes) Registration of new windows classes can include a request for up to 40 bytes of EWM to be appended to the allocated memory of each instance of that class. This EWM is intended to store data specific to that window and has specific application programming interface (API) functions to set and get its value. (Citation: Microsoft GetWindowLong function) (Citation: Microsoft SetWindowLong function)\n\nAlthough small, the EWM is large enough to store a 32-bit pointer and is often used to point to a windows procedure. Malware may possibly utilize this memory location in part of an attack chain that includes writing code to shared sections of the process’s memory, placing a pointer to the code in EWM, then invoking execution by returning execution control to the address in the process’s EWM.\n\nExecution granted through EWM injection may allow access to both the target process's memory and possibly elevated privileges. Writing payloads to shared sections also avoids the use of highly monitored API calls such as <code>WriteProcessMemory</code> and <code>CreateRemoteThread</code>.(Citation: Elastic Process Injection July 2017) More sophisticated malware samples may also potentially bypass protection mechanisms such as data execution prevention (DEP) by triggering a combination of windows procedures and other system functions that will rewrite the malicious payload inside an executable portion of the target process.  (Citation: MalwareTech Power Loader Aug 2013) (Citation: WeLiveSecurity Gapz and Redyms Mar 2013)\n\nRunning code in the context of another process may allow access to the process's memory, system/network resources, and possibly elevated privileges. Execution via EWM injection may also evade detection from security products since the execution is masked under a legitimate process. ",
    "external_references": [
      {
        "source_name": "mitre-attack",
        "external_id": "T1055.011",
        "url": "https://attack.mitre.org/techniques/T1055/011"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633574.aspx",
        "description": "Microsoft. (n.d.). About Window Classes. Retrieved December 16, 2017.",
        "source_name": "Microsoft Window Classes"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633584.aspx",
        "description": "Microsoft. (n.d.). GetWindowLong function. Retrieved December 16, 2017.",
        "source_name": "Microsoft GetWindowLong function"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms633591.aspx",
        "description": "Microsoft. (n.d.). SetWindowLong function. Retrieved December 16, 2017.",
        "source_name": "Microsoft SetWindowLong function"
      },
      {
        "url": "https://www.endgame.com/blog/technical-blog/ten-process-injection-techniques-technical-survey-common-and-trending-process",
        "description": "Hosseini, A. (2017, July 18). Ten Process Injection Techniques: A Technical Survey Of Common And Trending Process Injection Techniques. Retrieved December 7, 2017.",
        "source_name": "Elastic Process Injection July 2017"
      },
      {
        "url": "https://www.malwaretech.com/2013/08/powerloader-injection-something-truly.html",
        "description": "MalwareTech. (2013, August 13). PowerLoader Injection – Something truly amazing. Retrieved December 16, 2017.",
        "source_name": "MalwareTech Power Loader Aug 2013"
      },
      {
        "url": "https://www.welivesecurity.com/2013/03/19/gapz-and-redyms-droppers-based-on-power-loader-code/",
        "description": "Matrosov, A. (2013, March 19). Gapz and Redyms droppers based on Power Loader code. Retrieved December 16, 2017.",
        "source_name": "WeLiveSecurity Gapz and Redyms Mar 2013"
      },
      {
        "url": "https://msdn.microsoft.com/library/windows/desktop/ms644953.aspx",
        "description": "Microsoft. (n.d.). SendNotifyMessage function. Retrieved December 16, 2017.",
        "source_name": "Microsoft SendNotifyMessage function"
      }
    ],
    "id": "attack-pattern--0042a9f5-f053-4769-b3ef-9ad018dfa298",
    "kill_chain_phases": [
      {
        "kill_chain_name": "mitre-attack",
        "phase_name": "defense-evasion"
      },
      {
        "kill_chain_name": "mitre-attack",
        "phase_name": "privilege-escalation"
      }
    ],
    "modified": "2022-04-25T14:00:00.188Z",
    "name": "Extra Window Memory Injection",
    "object_marking_refs": [
      "marking-definition--fa42a846-8d90-4e51-bc29-71d5b4802168"
    ],
    "spec_version": "2.1",
    "type": "attack-pattern",
    "x_mitre_attack_spec_version": "2.1.0",
    "x_mitre_data_sources": [
      "Process: OS API Execution"
    ],
    "x_mitre_defense_bypassed": [
      "Anti-virus",
      "Application control"
    ],
    "x_mitre_detection": "Monitor for API calls related to enumerating and manipulating EWM such as GetWindowLong (Citation: Microsoft GetWindowLong function) and SetWindowLong (Citation: Microsoft SetWindowLong function). Malware associated with this technique have also used SendNotifyMessage (Citation: Microsoft SendNotifyMessage function) to trigger the associated window procedure and eventual malicious injection. (Citation: Elastic Process Injection July 2017)",
    "x_mitre_domains": [
      "enterprise-attack"
    ],
    "x_mitre_is_subtechnique": true,
    "x_mitre_modified_by_ref": "identity--c78cb6e5-0c4b-4611-8297-d1b8b55e40b5",
    "x_mitre_platforms": [
      "Windows"
    ],
    "x_mitre_version": "1.0"
  },
  {
    "created": "2020-01-01T00:00:00.000Z",
    "created_by_ref": "identity--8700e156-6ce9-5090-8589-f9d0aef7bdb7",
    "description": "Cheap fakes utilise less sophisticated measures of altering an image, video, or audio for example, slowing, speeding, or cutting footage to create a false context surrounding an image or event.",
    "external_references": [
      {
        "source_name": "DISARM",
        "url": "https://raw.githubusercontent.com/DISARMFoundation/DISARMframeworks/main/generated_pages/techniques/T0086.003.md",
        "external_id": "T0086.003"
      }
    ],
    "id": "attack-pattern--00dc0ed2-b16d-5f33-bad3-cc54fb7be6a9",
    "kill_chain_phases": [
      {
        "kill_chain_name": "disarm",
        "phase_name": "develop-content"
      }
    ],
    "modified": "2024-03-13T00:00:00.000Z",
    "name": "Deceptively Edit Images (Cheap Fakes)",
    "object_marking_refs": [
      "marking-definition--94868c89-83c2-464b-929b-a1a8aa3c8487",
      "marking-definition--8700e156-6ce9-5090-8589-f9d0aef7bdb7"
    ],
    "spec_version": "2.1",
    "type": "attack-pattern",
    "x_mitre_is_subtechnique": true,
    "x_mitre_platforms": [
      "Windows",
      "Linux",
      "Mac"
    ],
    "x_mitre_version": "2.1"
  },
  {
    "created": "2020-01-01T00:00:00.000Z",
    "created_by_ref": "identity--8700e156-6ce9-5090-8589-f9d0aef7bdb7",
    "description": "Cheap fakes utilise less sophisticated measures of altering an image, video, or audio for example, slowing, speeding, or cutting footage to create a false context surrounding an image or event.",
    "external_references": [
      {
        "source_name": "DISARM",
        "url": "https://raw.githubusercontent.com/DISARMFoundation/DISARMframeworks/main/generated_pages/techniques/T0086.003.md",
        "external_id": "T0086.003"
      }
    ],
    "id": "attack-pattern--00dc0ed2-b16d-5f33-bad3-cc54fb7be6a9",
    "kill_chain_phases": [
      {
        "kill_chain_name": "disarm",
        "phase_name": "develop-content"
      }
    ],
    "modified": "2024-08-02T00:00:00.000Z",
    "name": "Deceptively Edit Images (Cheap Fakes)",
    "object_marking_refs": [
      "marking-definition--94868c89-83c2-464b-929b-a1a8aa3c8487",
      "marking-definition--8700e156-6ce9-5090-8589-f9d0aef7bdb7"
    ],
    "spec_version": "2.1",
    "type": "attack-pattern",
    "x_mitre_is_subtechnique": true,
    "x_mitre_platforms": [
      "Windows",
      "Linux",
      "Mac"
    ],
    "x_mitre_version": "2.1"
  },
  {
    "created": "2020-01-01T00:00:00.000Z",
    "created_by_ref": "identity--8700e156-6ce9-5090-8589-f9d0aef7bdb7",
    "description": "Cheap fakes utilise less sophisticated measures of altering an image, video, or audio for example, slowing, speeding, or cutting footage to create a false context surrounding an image or event.",
    "external_references": [
      {
        "source_name": "DISARM",
        "url": "https://raw.githubusercontent.com/DISARMFoundation/DISARMframeworks/main/generated_pages/techniques/T0086.003.md",
        "external_id": "T0086.003"
      }
    ],
    "id": "attack-pattern--00dc0ed2-b16d-5f33-bad3-cc54fb7be6a9",
    "kill_chain_phases": [
      {
        "kill_chain_name": "disarm",
        "phase_name": "develop-content"
      }
    ],
    "modified": "2024-11-22T00:00:00.000Z",
    "name": "Deceptively Edit Images (Cheap Fakes)",
    "object_marking_refs": [
      "marking-definition--94868c89-83c2-464b-929b-a1a8aa3c8487",
      "marking-definition--8700e156-6ce9-5090-8589-f9d0aef7bdb7"
    ],
    "spec_version": "2.1",
    "type": "attack-pattern",
    "x_mitre_is_subtechnique": true,
    "x_mitre_platforms": [
      "Windows",
      "Linux",
      "Mac"
    ],
    "x_mitre_version": "2.1"
  },
  {
    "created": "2020-01-01T00:00:00.000Z",
    "created_by_ref": "identity--8700e156-6ce9-5090-8589-f9d0aef7bdb7",
    "description": "An influence operation may identify trending hashtags on social media platforms for later use in boosting operation content. A hashtag40 refers to a word or phrase preceded by the hash symbol (#) on social media used to identify messages and posts relating to a specific topic. All public posts that use the same hashtag are aggregated onto a centralised page dedicated to the word or phrase and sorted either chronologically or by popularity.",
    "external_references": [
      {
        "source_name": "DISARM",
        "url": "https://raw.githubusercontent.com/DISARMFoundation/DISARMframeworks/main/generated_pages/techniques/T0080.003.md",
        "external_id": "T0080.003"
      }
    ],
    "id": "attack-pattern--00e4fd6f-7fcd-56d0-be21-5d61dc2c6a5a",
    "kill_chain_phases": [
      {
        "kill_chain_name": "disarm",
        "phase_name": "target-audience-analysis"
      }
    ],
    "modified": "2024-03-13T00:00:00.000Z",
    "name": "Identify Trending Topics/Hashtags",
    "object_marking_refs": [
      "marking-definition--94868c89-83c2-464b-929b-a1a8aa3c8487",
      "marking-definition--8700e156-6ce9-5090-8589-f9d0aef7bdb7"
    ],
    "spec_version": "2.1",
    "type": "attack-pattern",
    "x_mitre_is_subtechnique": true,
    "x_mitre_platforms": [
      "Windows",
      "Linux",
      "Mac"
    ],
    "x_mitre_version": "2.1"
  },
  {
    "created": "2020-01-01T00:00:00.000Z",
    "created_by_ref": "identity--8700e156-6ce9-5090-8589-f9d0aef7bdb7",
    "description": "An influence operation may identify trending hashtags on social media platforms for later use in boosting operation content. A hashtag40 refers to a word or phrase preceded by the hash symbol (#) on social media used to identify messages and posts relating to a specific topic. All public posts that use the same hashtag are aggregated onto a centralised page dedicated to the word or phrase and sorted either chronologically or by popularity.",
    "external_references": [
      {
        "source_name": "DISARM",
        "url": "https://raw.githubusercontent.com/DISARMFoundation/DISARMframeworks/main/generated_pages/techniques/T0080.003.md",
        "external_id": "T0080.003"
      }
    ],
    "id": "attack-pattern--00e4fd6f-7fcd-56d0-be21-5d61dc2c6a5a",
    "kill_chain_phases": [
      {
        "kill_chain_name": "disarm",
        "phase_name": "target-audience-analysis"
      }
    ],
    "modified": "2024-08-02T00:00:00.000Z",
    "name": "Identify Trending Topics/Hashtags",
    "object_marking_refs": [
      "marking-definition--94868c89-83c2-464b-929b-a1a8aa3c8487",
      "marking-definition--8700e156-6ce9-5090-8589-f9d0aef7bdb7"
    ],
    "spec_version": "2.1",
    "type": "attack-pattern",
    "x_mitre_is_subtechnique": true,
    "x_mitre_platforms": [
      "Windows",
      "Linux",
      "Mac"
    ],
    "x_mitre_version": "2.1"
  },
  {
    "created": "2020-01-01T00:00:00.000Z",
    "created_by_ref": "identity--8700e156-6ce9-5090-8589-f9d0aef7bdb7",
    "description": "An influence operation may identify trending hashtags on social media platforms for later use in boosting operation content. A hashtag40 refers to a word or phrase preceded by the hash symbol (#) on social media used to identify messages and posts relating to a specific topic. All public posts that use the same hashtag are aggregated onto a centralised page dedicated to the word or phrase and sorted either chronologically or by popularity.",
    "external_references": [
      {
        "source_name": "DISARM",
        "url": "https://raw.githubusercontent.com/DISARMFoundation/DISARMframeworks/main/generated_pages/techniques/T0080.003.md",
        "external_id": "T0080.003"
      }
    ],
    "id": "attack-pattern--00e4fd6f-7fcd-56d0-be21-5d61dc2c6a5a",
    "kill_chain_phases": [
      {
        "kill_chain_name": "disarm",
        "phase_name": "target-audience-analysis"
      }
    ],
    "modified": "2024-11-22T00:00:00.000Z",
    "name": "Identify Trending Topics/Hashtags",
    "object_marking_refs": [
      "marking-definition--94868c89-83c2-464b-929b-a1a8aa3c8487",
      "marking-definition--8700e156-6ce9-5090-8589-f9d0aef7bdb7"
    ],
    "spec_version": "2.1",
    "type": "attack-pattern",
    "x_mitre_is_subtechnique": true,
    "x_mitre_platforms": [
      "Windows",
      "Linux",
      "Mac"
    ],
    "x_mitre_version": "2.1"
  },
  {
    "created": "2014-06-23T00:00:00.000Z",
    "created_by_ref": "identity--e50ab59c-5c4f-4d40-bf6a-d58418d89bcd",
    "description": "An attacker uses deceptive methods to cause a user or an automated process to download and install dangerous code that originates from an attacker controlled source. There are several variations to this strategy of attack.",
    "external_references": [
      {
        "external_id": "CAPEC-185",
        "source_name": "capec",
        "url": "https://capec.mitre.org/data/definitions/185.html"
      },
      {
        "external_id": "CWE-494",
        "source_name": "cwe",
        "url": "http://cwe.mitre.org/data/definitions/494.html"
      },
      {
        "description": "Ingress Tool Transfer",
        "external_id": "T1105",
        "source_name": "ATTACK",
        "url": "https://attack.mitre.org/wiki/Technique/T1105"
      }
    ],
    "id": "attack-pattern--0123fa83-2d47-4398-85f1-30ce114abb9a",
    "modified": "2021-06-24T00:00:00.000Z",
    "name": "Malicious Software Download",
    "object_marking_refs": [
      "marking-definition--17d82bb2-eeeb-4898-bda5-3ddbcd2b799d"
    ],
    "spec_version": "2.1",
    "type": "attack-pattern",
    "x_capec_abstraction": "Standard",
    "x_capec_can_follow_refs": [
      "attack-pattern--d16af13f-5e0f-4a6b-bc1f-23f733d2229b"
    ],
    "x_capec_can_precede_refs": [
      "attack-pattern--558870ad-9433-4e39-a0b0-d9b5c4691862"
    ],
    "x_capec_child_of_refs": [
      "attack-pattern--582f33d6-0aa7-4f34-a91e-d767a65adad1"
    ],
    "x_capec_status": "Draft",
    "x_capec_typical_severity": "Very High",
    "x_capec_version": "3.5"
  },
  {
    "created": "2014-06-23T00:00:00.000Z",
    "created_by_ref": "identity--e50ab59c-5c4f-4d40-bf6a-d58418d89bcd",
    "description": "An attacker uses deceptive methods to cause a user or an automated process to download and install dangerous code that originates from an attacker controlled source. There are several variations to this strategy of attack.",
    "external_references": [
      {
        "external_id": "CAPEC-185",
        "source_name": "capec",
        "url": "https://capec.mitre.org/data/definitions/185.html"
      },
      {
        "external_id": "CWE-494",
        "source_name": "cwe",
        "url": "http://cwe.mitre.org/data/definitions/494.html"
      },
      {
        "description": "Ingress Tool Transfer",
        "external_id": "T1105",
        "source_name": "ATTACK",
        "url": "https://attack.mitre.org/wiki/Technique/T1105"
      }
    ],
    "id": "attack-pattern--0123fa83-2d47-4398-85f1-30ce114abb9a",
    "modified": "2021-06-24T00:00:00.000Z",
    "name": "Malicious Software Download",
    "object_marking_refs": [
      "marking-definition--17d82bb2-eeeb-4898-bda5-3ddbcd2b799d"
    ],
    "spec_version": "2.1",
    "type": "attack-pattern",
    "x_capec_abstraction": "Standard",
    "x_capec_can_follow_refs": [
      "attack-pattern--d16af13f-5e0f-4a6b-bc1f-23f733d2229b"
    ],
    "x_capec_can_precede_refs": [
      "attack-pattern--558870ad-9433-4e39-a0b0-d9b5c4691862"
    ],
    "x_capec_child_of_refs": [
      "attack-pattern--582f33d6-0aa7-4f34-a91e-d767a65adad1"
    ],
    "x_capec_status": "Draft",
    "x_capec_typical_severity": "Very High",
    "x_capec_version": "3.6"
  },
  {
    "created": "2014-06-23T00:00:00.000Z",
    "created_by_ref": "identity--e50ab59c-5c4f-4d40-bf6a-d58418d89bcd",
    "description": "An attacker uses deceptive methods to cause a user or an automated process to download and install dangerous code that originates from an attacker controlled source. There are several variations to this strategy of attack.",
    "external_references": [
      {
        "external_id": "CAPEC-185",
        "source_name": "capec",
        "url": "https://capec.mitre.org/data/definitions/185.html"
      },
      {
        "external_id": "CWE-494",
        "source_name": "cwe",
        "url": "http://cwe.mitre.org/data/definitions/494.html"
      },
      {
        "description": "Ingress Tool Transfer",
        "external_id": "T1105",
        "source_name": "ATTACK",
        "url": "https://attack.mitre.org/wiki/Technique/T1105"
      }
    ],
    "id": "attack-pattern--0123fa83-2d47-4398-85f1-30ce114abb9a",
    "modified": "2022-02-22T00:00:00.000Z",
    "name": "Malicious Software Download",
    "object_marking_refs": [
      "marking-definition--17d82bb2-eeeb-4898-bda5-3ddbcd2b799d"
    ],
    "spec_version": "2.1",
    "type": "attack-pattern",
    "x_capec_abstraction": "Standard",
    "x_capec_can_follow_refs": [
      "attack-pattern--d16af13f-5e0f-4a6b-bc1f-23f733d2229b"
    ],
    "x_capec_can_precede_refs": [
      "attack-pattern--558870ad-9433-4e39-a0b0-d9b5c4691862"
    ],
    "x_capec_child_of_refs": [
      "attack-pattern--582f33d6-0aa7-4f34-a91e-d767a65adad1"
    ],
    "x_capec_domains": [
      "Software"
    ],
    "x_capec_status": "Draft",
    "x_capec_typical_severity": "Very High",
    "x_capec_version": "3.7"
  },
  {
    "created": "2014-06-23T00:00:00.000Z",
    "created_by_ref": "identity--e50ab59c-5c4f-4d40-bf6a-d58418d89bcd",
    "description": "An attacker uses deceptive methods to cause a user or an automated process to download and install dangerous code that originates from an attacker controlled source. There are several variations to this strategy of attack.",
    "external_references": [
      {
        "external_id": "CAPEC-185",
        "source_name": "capec",
        "url": "https://capec.mitre.org/data/definitions/185.html"
      },
      {
        "external_id": "CWE-494",
        "source_name": "cwe",
        "url": "http://cwe.mitre.org/data/definitions/494.html"
      }
    ],
    "id": "attack-pattern--0123fa83-2d47-4398-85f1-30ce114abb9a",
    "modified": "2022-09-29T00:00:00.000Z",
    "name": "Malicious Software Download",
    "object_marking_refs": [
      "marking-definition--17d82bb2-eeeb-4898-bda5-3ddbcd2b799d"
    ],
    "spec_version": "2.1",
    "type": "attack-pattern",
    "x_capec_abstraction": "Standard",
    "x_capec_can_follow_refs": [
      "attack-pattern--d16af13f-5e0f-4a6b-bc1f-23f733d2229b"
    ],
    "x_capec_can_precede_refs": [
      "attack-pattern--558870ad-9433-4e39-a0b0-d9b5c4691862"
    ],
    "x_capec_child_of_refs": [
      "attack-pattern--582f33d6-0aa7-4f34-a91e-d767a65adad1"
    ],
    "x_capec_domains": [
      "Software"
    ],
    "x_capec_status": "Draft",
    "x_capec_typical_severity": "Very High",
    "x_capec_version": "3.8"
  },
  {
    "created": "2014-06-23T00:00:00.000Z",
    "created_by_ref": "identity--e50ab59c-5c4f-4d40-bf6a-d58418d89bcd",
    "description": "An attacker uses deceptive methods to cause a user or an automated process to download and install dangerous code that originates from an attacker controlled source. There are several variations to this strategy of attack.",
    "external_references": [
      {
        "external_id": "CAPEC-185",
        "source_name": "capec",
        "url": "https://capec.mitre.org/data/definitions/185.html"
      },
      {
        "external_id": "CWE-494",
        "source_name": "cwe",
        "url": "http://cwe.mitre.org/data/definitions/494.html"
      }
    ],
    "id": "attack-pattern--0123fa83-2d47-4398-85f1-30ce114abb9a",
    "modified": "2022-09-29T00:00:00.000Z",
    "name": "Malicious Software Download",
    "object_marking_refs": [
      "marking-definition--17d82bb2-eeeb-4898-bda5-3ddbcd2b799d"
    ],
    "spec_version": "2.1",
    "type": "attack-pattern",
    "x_capec_abstraction": "Standard",
    "x_capec_can_follow_refs": [
      "attack-pattern--d16af13f-5e0f-4a6b-bc1f-23f733d2229b"
    ],
    "x_capec_can_precede_refs": [
      "attack-pattern--558870ad-9433-4e39-a0b0-d9b5c4691862"
    ],
    "x_capec_child_of_refs": [
      "attack-pattern--582f33d6-0aa7-4f34-a91e-d767a65adad1"
    ],
    "x_capec_domains": [
      "Software"
    ],
    "x_capec_status": "Draft",
    "x_capec_typical_severity": "Very High",
    "x_capec_version": "3.9"
  },
  {
    "created": "2020-01-01T00:00:00.000Z",
    "created_by_ref": "identity--8700e156-6ce9-5090-8589-f9d0aef7bdb7",
    "description": "Co-Opt Grassroots Groups",
    "external_references": [
      {
        "source_name": "DISARM",
        "url": "https://raw.githubusercontent.com/DISARMFoundation/DISARMframeworks/main/generated_pages/techniques/T0100.002.md",
        "external_id": "T0100.002"
      }
    ],
    "id": "attack-pattern--01c870a4-50d9-563b-81a8-512b36e12af4",
    "kill_chain_phases": [
      {
        "kill_chain_name": "disarm",
        "phase_name": "establish-legitimacy"
      }
    ],
    "modified": "2024-03-13T00:00:00.000Z",
    "name": "Co-Opt Grassroots Groups",
    "object_marking_refs": [
      "marking-definition--94868c89-83c2-464b-929b-a1a8aa3c8487",
      "marking-definition--8700e156-6ce9-5090-8589-f9d0aef7bdb7"
    ],
    "spec_version": "2.1",
    "type": "attack-pattern",
    "x_mitre_is_subtechnique": true,
    "x_mitre_platforms": [
      "Windows",
      "Linux",
      "Mac"
    ],
    "x_mitre_version": "2.1"
  },
  {
    "created": "2020-01-01T00:00:00.000Z",
    "created_by_ref": "identity--8700e156-6ce9-5090-8589-f9d0aef7bdb7",
    "description": "Co-Opt Grassroots Groups",
    "external_references": [
      {
        "source_name": "DISARM",
        "url": "https://raw.githubusercontent.com/DISARMFoundation/DISARMframeworks/main/generated_pages/techniques/T0100.002.md",
        "external_id": "T0100.002"
      }
    ],
    "id": "attack-pattern--01c870a4-50d9-563b-81a8-512b36e12af4",
    "kill_chain_phases": [
      {
        "kill_chain_name": "disarm",
        "phase_name": "establish-legitimacy"
      }
    ],
    "modified": "2024-08-02T00:00:00.000Z",
    "name": "Co-Opt Grassroots Groups",
    "object_marking_refs": [
      "marking-definition--94868c89-83c2-464b-929b-a1a8aa3c8487",
      "marking-definition--8700e156-6ce9-5090-8589-f9d0aef7bdb7"
    ],
    "spec_version": "2.1",
    "type": "attack-pattern",
    "x_mitre_is_subtechnique": true,
    "x_mitre_platforms": [
      "Windows",
      "Linux",
      "Mac"
    ],
    "x_mitre_version": "2.1"
  },
  {
    "created": "2020-01-01T00:00:00.000Z",
    "created_by_ref": "identity--8700e156-6ce9-5090-8589-f9d0aef7bdb7",
    "description": "Co-Opt Grassroots Groups",
    "external_references": [
      {
        "source_name": "DISARM",
        "url": "https://raw.githubusercontent.com/DISARMFoundation/DISARMframeworks/main/generated_pages/techniques/T0100.002.md",
        "external_id": "T0100.002"
      }
    ],
    "id": "attack-pattern--01c870a4-50d9-563b-81a8-512b36e12af4",
    "kill_chain_phases": [
      {
        "kill_chain_name": "disarm",
        "phase_name": "establish-legitimacy"
      }
    ],
    "modified": "2024-11-22T00:00:00.000Z",
    "name": "Co-Opt Grassroots Groups",
    "object_marking_refs": [
      "marking-definition--94868c89-83c2-464b-929b-a1a8aa3c8487",
      "marking-definition--8700e156-6ce9-5090-8589-f9d0aef7bdb7"
    ],
    "spec_version": "2.1",
    "type": "attack-pattern",
    "x_mitre_is_subtechnique": true,
    "x_mitre_platforms": [
      "Windows",
      "Linux",
      "Mac"
    ],
    "x_mitre_version": "2.1"
  }
]


import json
from pathlib import Path
import random
bundle1 = {}
bundle2 = {}
bundle3 = {}

def fill_bundle(length):
    # for collection in [attack_patterns, weaknesses]:
    retval = {}
    while len(retval) < length:
        for c in [attack_patterns, weaknesses]:
            obj = random.choice(c)
            c.remove(obj)
            retval[obj['id']] = obj
    return list(retval.values())[:length]

def hash_bundle(b):
    return tuple((obj['id'], obj['modified']) for obj in b)

bundles = dict(bundle1=fill_bundle(6), bundle2=fill_bundle(3), bundle3=fill_bundle(4))

def write_bundle(bundles: dict):
    for k, v in bundles.items():
        path = Path(f'tests/bundles/{k}.json')
        path.parent.mkdir(exist_ok=True, parents=True)
        with path.open('w') as f:
            json.dump(dict(objects=v), f, indent=4)

write_bundle(bundles)