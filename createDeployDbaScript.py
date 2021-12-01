#----------------------------------------------------------------------------
# Script for create deploy_dba.sql and deploy_dba.zip files
# Run it within the folder that contains all the sql packages to be deployed
# Created by Esteban Salmeron - 2021
# V1.0    30-11-2021  Creation
#----------------------------------------------------------------------------

import os
import zipfile

# Type US info here!
print("Enter User Story info (ISITF XXX - Exciting task)")
userStory = input() + '\n'

zip = zipfile.ZipFile('deploy_dba.zip','a')
f = open('deploy_dba.sql', 'w')

f.write('--'+ userStory)
f.write('prompt SALES TEAM deployment starting \n')
f.write('set define off \n')
f.write('\n')

for root, dirs, files in os.walk('./'):
    for newname in files:
        filename = os.path.join(newname)
        if filename != 'deploy_dba.sql' and filename.endswith('.sql'):
            zip.write(filename)
            newstring = 'prompt ' + filename + '\n' + '@' + filename + '\n' + '\n'
            f.write(newstring)

f.close()
zip.write('deploy_dba.sql')
zip.close()