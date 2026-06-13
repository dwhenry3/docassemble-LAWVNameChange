import os
import sys
from setuptools import setup, find_namespace_packages
from fnmatch import fnmatchcase
from distutils.util import convert_path

standard_exclude = ('*.pyc', '*~', '.*', '*.bak', '*.swp*')
standard_exclude_directories = ('.*', 'CVS', '_darcs', './build', './dist', 'EGG-INFO', '*.egg-info')

def find_package_data(where='.', package='', exclude=standard_exclude, exclude_directories=standard_exclude_directories):
    out = {}
    stack = [(convert_path(where), '', package)]
    while stack:
        where, prefix, package = stack.pop(0)
        for name in os.listdir(where):
            fn = os.path.join(where, name)
            if os.path.isdir(fn):
                bad_name = False
                for pattern in exclude_directories:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                if os.path.isfile(os.path.join(fn, '__init__.py')):
                    if not package:
                        new_package = name
                    else:
                        new_package = package + '.' + name
                        stack.append((fn, '', new_package))
                else:
                    stack.append((fn, prefix + name + '/', package))
            else:
                bad_name = False
                for pattern in exclude:
                    if (fnmatchcase(name, pattern)
                        or fn.lower() == pattern.lower()):
                        bad_name = True
                        break
                if bad_name:
                    continue
                out.setdefault(package, []).append(prefix+name)
    return out

setup(name='docassemble.LAWVNameChange',
      version='1.0.12',
      description=('A docassemble extension.'),
      long_description='# Name Change Petition Interview\r\n\r\nA **Docassemble** interview designed by **Legal Aid of West Virginia** to help self-represented litigants generate a complete **Name Change Packet**, including all required pleadings and filing instructions for West Virginia circuit or family courts.\r\n\r\nThis interview collects the user’s information, screens for eligibility, and produces a bundled PDF package containing:\r\n\r\n- Name Change Instructions  \r\n- Civil Case Information Statement (Circuit or Family)  \r\n- Petition for Name Change  \r\n- Order Filing Petition  \r\n- Order of Publication  \r\n- Final Name Change Order  \r\n\r\n---\r\n\r\n## Purpose\r\n\r\nThis tool assists individuals seeking an adult name change in West Virginia. It guides the user through the required legal questions, helps determine eligibility, and generates all necessary forms for filing with the appropriate county clerk.\r\n\r\n---\r\n\r\n## Features\r\n\r\n### User-Facing Features\r\n\r\n- Residency and eligibility screening  \r\n- Guided data collection for current name, birth name, and desired new name  \r\n- Optional identity protection request  \r\n- Optional courtroom accommodation requests  \r\n- Automated courthouse and local library lookup based on address  \r\n- Step-by-step filing instructions  \r\n- Automatic PDF packet generation  \r\n- Optional email delivery of completed forms  \r\n\r\n### Technical Features\r\n\r\n- Uses **docassemble.LAWVCommon** for styling, validation, and shared components  \r\n- Geolocation and distance calculations via **geopy**  \r\n- Progressive disclosure for improved accessibility  \r\n- Automatic formatting of telephone numbers and state selections  \r\n- Dynamic PDF and DOCX generation through Docassemble templates  \r\n- Code-driven determination of filing court (Family or Circuit)  \r\n- Conditional logic for ineligibility endpoints  \r\n\r\n---\r\n\r\n## File Information\r\n\r\nThis repository includes the Docassemble interview YAML file:\r\n\r\n- `name_change.yml` — Main interview file controlling logic, questions, attachments, validations, and document output.\r\n\r\nAssociated templates referenced in the YAML should be included within the Docassemble package, such as:\r\n\r\n- `name_change_instructions.pdf`  \r\n- `name_change_petition_adult.docx`  \r\n- `name_change_order_of_publication.docx`  \r\n- `name_change_order_filing_petition.docx`  \r\n- `name_change_order.docx`  \r\n- Civil and domestic case information templates from `docassemble.LAWVCommon`  \r\n\r\n---\r\n\r\n## Running the Interview\r\n\r\nAfter deployment, access the interview through your Docassemble server interface or direct interview URL.  \r\nThe user will proceed through structured questions that populate the generated PDF packet.\r\n\r\n---\r\n\r\n## Logic Overview\r\n\r\nThe interview performs the following major steps:\r\n\r\n1. Residency check: County and state residency of at least one year  \r\n2. Eligibility screen: Ensures no prohibited reasons for the name change  \r\n3. Collect personal and birth information  \r\n4. Collect desired new name  \r\n5. Require a reason for the name change  \r\n6. Optional identity protection request  \r\n7. Optional ADA accommodations  \r\n8. Determine court type: Family or Circuit  \r\n9. Assign correct courthouse and nearest library  \r\n10. Generate documents  \r\n11. Package output  \r\n12. Email documents (optional)  \r\n\r\nIf the user is ineligible, the interview stops and displays a message encouraging them to seek legal assistance.\r\n\r\n---\r\n\r\n## Output\r\n\r\nThe interview generates a **Name Change Packet.zip** containing:\r\n\r\n- PDFs of all required documents  \r\n- Filing instructions and address information  \r\n\r\nAll personal information is purged upon exiting the interview.\r\n\r\n---\r\n\r\n## Contact\r\n\r\nCreated by **Dane W. Henry, Esq.** for **Legal Aid of West Virginia**.  \r\n\r\nGeneral assistance: https://legalaidwv.org/',
      long_description_content_type='text/markdown',
      author='Dane W. Henry, Esq.',
      author_email='dhenry@lawv.net',
      license='MIT',
      url='https://docassemble.org',
      packages=find_namespace_packages(),
      install_requires=[],
      zip_safe=False,
      package_data=find_package_data(where='docassemble/LAWVNameChange/', package='docassemble.LAWVNameChange'),
     )
