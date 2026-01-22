# Name Change Petition Interview

A **Docassemble** interview designed by **Legal Aid of West Virginia** to help self-represented litigants generate a complete **Name Change Packet**, including all required pleadings and filing instructions for West Virginia circuit or family courts.

This interview collects the user’s information, screens for eligibility, and produces a bundled PDF package containing:

- Name Change Instructions  
- Civil Case Information Statement (Circuit or Family)  
- Petition for Name Change  
- Order Filing Petition  
- Order of Publication  
- Final Name Change Order  

---

## Purpose

This tool assists individuals seeking an adult name change in West Virginia. It guides the user through the required legal questions, helps determine eligibility, and generates all necessary forms for filing with the appropriate county clerk.

---

## Features

### User-Facing Features

- Residency and eligibility screening  
- Guided data collection for current name, birth name, and desired new name  
- Optional identity protection request  
- Optional courtroom accommodation requests  
- Automated courthouse and local library lookup based on address  
- Step-by-step filing instructions  
- Automatic PDF packet generation  
- Optional email delivery of completed forms  

### Technical Features

- Uses **docassemble.LAWVCommon** for styling, validation, and shared components  
- Geolocation and distance calculations via **geopy**  
- Progressive disclosure for improved accessibility  
- Automatic formatting of telephone numbers and state selections  
- Dynamic PDF and DOCX generation through Docassemble templates  
- Code-driven determination of filing court (Family or Circuit)  
- Conditional logic for ineligibility endpoints  

---

## File Information

This repository includes the Docassemble interview YAML file:

- `name_change.yml` — Main interview file controlling logic, questions, attachments, validations, and document output.

Associated templates referenced in the YAML should be included within the Docassemble package, such as:

- `name_change_instructions.pdf`  
- `name_change_petition_adult.docx`  
- `name_change_order_of_publication.docx`  
- `name_change_order_filing_petition.docx`  
- `name_change_order.docx`  
- Civil and domestic case information templates from `docassemble.LAWVCommon`  

---

## Running the Interview

After deployment, access the interview through your Docassemble server interface or direct interview URL.  
The user will proceed through structured questions that populate the generated PDF packet.

---

## Logic Overview

The interview performs the following major steps:

1. Residency check: County and state residency of at least one year  
2. Eligibility screen: Ensures no prohibited reasons for the name change  
3. Collect personal and birth information  
4. Collect desired new name  
5. Require a reason for the name change  
6. Optional identity protection request  
7. Optional ADA accommodations  
8. Determine court type: Family or Circuit  
9. Assign correct courthouse and nearest library  
10. Generate documents  
11. Package output  
12. Email documents (optional)  

If the user is ineligible, the interview stops and displays a message encouraging them to seek legal assistance.

---

## Output

The interview generates a **Name Change Packet.zip** containing:

- PDFs of all required documents  
- Filing instructions and address information  

All personal information is purged upon exiting the interview.

---

## Contact

Created by **Dane W. Henry, Esq.** for **Legal Aid of West Virginia**.  

General assistance: https://legalaidwv.org/