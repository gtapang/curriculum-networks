#!/bin/bash
# Download all UP Diliman undergraduate curriculum checklists
# Generated from 78 programs

mkdir -p checklists
cd checklists || exit 1

# Anthropology
curl -fSL -o "Anthropology.pdf" "https://our.upd.edu.ph/files/Checklist/UG/CSSP/CSSP_Bachelor%20of%20Arts%20%28Anthropology%29.pdf" || echo "FAILED: Anthropology"

# Applied Physics
curl -fSL -o "Applied_Physics.pdf" "https://our.upd.edu.ph/files/Checklist/UG/CS/CS_Bachelor%20of%20Science%20in%20Applied%20Physics.pdf" || echo "FAILED: Applied Physics"

# Applied Psychology (UPDEPPO)
curl -fSL -o "Applied_Psychology_(UPDEPPO).pdf" "https://our.upd.edu.ph/files/Checklist/UG/UPDEPP/UPDEPP_Bachelor%20of%20Arts%20%28Applied%20Psychology%29.pdf" || echo "FAILED: Applied Psychology (UPDEPPO)"

# Architecture
curl -fSL -o "Architecture.pdf" "https://our.upd.edu.ph/files/Checklist/UG/CA/CA_Bachelor%20of%20Science%20in%20Architecture.pdf" || echo "FAILED: Architecture"

# Art Education
curl -fSL -o "Art_Education.pdf" "https://our.upd.edu.ph/files/Checklist/UG/CFA/CFA_Bachelor%20of%20Fine%20Arts%20%28Art%20Education%29.pdf" || echo "FAILED: Art Education"

# Art History
curl -fSL -o "Art_History.pdf" "https://our.upd.edu.ph/files/Checklist/UG/CFA/CFA_Bachelor%20of%20Fine%20Arts%20%28Art%20History%29.pdf" || echo "FAILED: Art History"

# Art Studies
curl -fSL -o "Art_Studies.pdf" "https://our.upd.edu.ph/files/Checklist/UG/CAL/CAL_Bachelor%20of%20Arts%20%28Art%20Studies%29.pdf" || echo "FAILED: Art Studies"

# Biology
curl -fSL -o "Biology.pdf" "https://our.upd.edu.ph/files/Checklist/UG/CS/CS_Bachelor%20of%20Science%20in%20Biology.pdf" || echo "FAILED: Biology"

# Broadcast Communication
curl -fSL -o "Broadcast_Communication.pdf" "https://our.upd.edu.ph/files/Checklist/UG/CMC/CMC_Bachelor%20of%20Arts%20in%20Broadcast%20Communication.pdf" || echo "FAILED: Broadcast Communication"

# Building Technology
curl -fSL -o "Building_Technology.pdf" "https://our.upd.edu.ph/files/Checklist/UG/CA/CA_Certificate%20in%20Building%20Technology.pdf" || echo "FAILED: Building Technology"

# Business Administration
curl -fSL -o "Business_Administration.pdf" "https://our.upd.edu.ph/files/Checklist/UG/VSB/VSB_Bachelor%20of%20Science%20in%20Business%20Administration.pdf" || echo "FAILED: Business Administration"

# Business Administration and Accountancy
curl -fSL -o "Business_Administration_and_Accountancy.pdf" "https://our.upd.edu.ph/files/Checklist/UG/VSB/VSB_Bachelor%20of%20Science%20in%20Business%20Administration%20and%20Accountancy.pdf" || echo "FAILED: Business Administration and Accountancy"

# Business Economics
curl -fSL -o "Business_Economics.pdf" "https://our.upd.edu.ph/files/Checklist/UG/SE/SE_Bachelor%20of%20Science%20in%20Business%20Economics.pdf" || echo "FAILED: Business Economics"

# Business Economics (UPDEPPO)
curl -fSL -o "Business_Economics_(UPDEPPO).pdf" "https://our.upd.edu.ph/files/Checklist/UG/UPDEPP/UPDEPP_Bachelor%20of%20Science%20in%20Business%20Economics.pdf" || echo "FAILED: Business Economics (UPDEPPO)"

# Business Management (UPDEPPO)
curl -fSL -o "Business_Management_(UPDEPPO).pdf" "https://our.upd.edu.ph/files/Checklist/UG/UPDEPP/UPDEPP_Bachelor%20of%20Science%20in%20Business%20Management.pdf" || echo "FAILED: Business Management (UPDEPPO)"

# Chemical Engineering
curl -fSL -o "Chemical_Engineering.pdf" "https://our.upd.edu.ph/files/Checklist/UG/COE/COE_Bachelor%20of%20Science%20in%20Chemical%20Engineering.pdf" || echo "FAILED: Chemical Engineering"

# Chemistry
curl -fSL -o "Chemistry.pdf" "https://our.upd.edu.ph/files/Checklist/UG/CS/CS_Bachelor%20of%20Science%20in%20Chemistry.pdf" || echo "FAILED: Chemistry"

# Civil Engineering
curl -fSL -o "Civil_Engineering.pdf" "https://our.upd.edu.ph/files/Checklist/UG/COE/COE_Bachelor%20of%20Science%20in%20Civil%20Engineering.pdf" || echo "FAILED: Civil Engineering"

# Clothing Technology
curl -fSL -o "Clothing_Technology.pdf" "https://our.upd.edu.ph/files/Checklist/UG/CHE/CHE_Bachelor%20of%20Science%20in%20Clothing%20Technology.pdf" || echo "FAILED: Clothing Technology"

# Community Development
curl -fSL -o "Community_Development.pdf" "https://our.upd.edu.ph/files/Checklist/UG/CSWCD/CSWCD_Bachelor%20of%20Science%20in%20Community%20Development.pdf" || echo "FAILED: Community Development"

# Communication Research
curl -fSL -o "Communication_Research.pdf" "https://our.upd.edu.ph/files/Checklist/UG/CMC/CMC_Bachelor%20of%20Arts%20in%20Communication%20Research.pdf" || echo "FAILED: Communication Research"

# Community Nutrition
curl -fSL -o "Community_Nutrition.pdf" "https://our.upd.edu.ph/files/Checklist/UG/CHE/CHE_Bachelor%20of%20Science%20in%20Community%20Nutrition.pdf" || echo "FAILED: Community Nutrition"

# Comparative Literature
curl -fSL -o "Comparative_Literature.pdf" "https://our.upd.edu.ph/files/Checklist/UG/CAL/CAL_Bachelor%20of%20Arts%20%28Comparative%20Literature%29.pdf" || echo "FAILED: Comparative Literature"

# Computer Engineering
curl -fSL -o "Computer_Engineering.pdf" "https://our.upd.edu.ph/files/Checklist/UG/COE/COE_Bachelor%20of%20Science%20in%20Computer%20Engineering.pdf" || echo "FAILED: Computer Engineering"

# Computer Science
curl -fSL -o "Computer_Science.pdf" "https://our.upd.edu.ph/files/Checklist/UG/COE/COE_Bachelor%20of%20Science%20in%20Computer%20Science.pdf" || echo "FAILED: Computer Science"

# Creative Writing
curl -fSL -o "Creative_Writing.pdf" "https://our.upd.edu.ph/files/Checklist/UG/CAL/CAL_Bachelor%20of%20Arts%20%28Creative%20Writing%29.pdf" || echo "FAILED: Creative Writing"

# Economics
curl -fSL -o "Economics.pdf" "https://our.upd.edu.ph/files/Checklist/UG/SE/SE_Bachelor%20of%20Science%20in%20Economics.pdf" || echo "FAILED: Economics"

# Electrical Engineering
curl -fSL -o "Electrical_Engineering.pdf" "https://our.upd.edu.ph/files/Checklist/UG/COE/COE_Bachelor%20of%20Science%20in%20Electrical%20Engineering.pdf" || echo "FAILED: Electrical Engineering"

# Electronics Engineering
curl -fSL -o "Electronics_Engineering.pdf" "https://our.upd.edu.ph/files/Checklist/UG/COE/COE_Bachelor%20of%20Science%20in%20Electronics%20and%20Communications%20Engineering.pdf" || echo "FAILED: Electronics Engineering"

# Elementary Education
curl -fSL -o "Elementary_Education.pdf" "https://our.upd.edu.ph/files/Checklist/UG/EDUC/EDUC_Bachelor%20of%20Elementary%20Education.pdf" || echo "FAILED: Elementary Education"

# English Studies: Language
curl -fSL -o "English_Studies:_Language.pdf" "https://our.upd.edu.ph/files/Checklist/UG/CAL/CAL_Bachelor%20of%20Arts%20%28English%20Studies%29.pdf" || echo "FAILED: English Studies: Language"

# English Studies: Literature
curl -fSL -o "English_Studies:_Literature.pdf" "https://our.upd.edu.ph/files/Checklist/UG/CAL/CAL_Bachelor%20of%20Arts%20%28English%20Studies%29.pdf" || echo "FAILED: English Studies: Literature"

# European Languages
curl -fSL -o "European_Languages.pdf" "https://our.upd.edu.ph/files/Checklist/UG/CAL/CAL_Bachelor%20of%20Arts%20%28European%20Languages%29.pdf" || echo "FAILED: European Languages"

# Family Life and Child Development
curl -fSL -o "Family_Life_and_Child_Development.pdf" "https://our.upd.edu.ph/files/Checklist/UG/CHE/CHE_Bachelor%20of%20Science%20in%20Family%20Life%20and%20Child%20Development.pdf" || echo "FAILED: Family Life and Child Development"

# Filipino
curl -fSL -o "Filipino.pdf" "https://our.upd.edu.ph/files/Checklist/UG/CAL/CAL_Bachelor%20of%20Arts%20%28Filipino%20at%20Panitikan%20ng%20Pilipinas%29.pdf" || echo "FAILED: Filipino"

# Film
curl -fSL -o "Film.pdf" "https://our.upd.edu.ph/files/Checklist/UG/CMC/CMC_Bachelor%20of%20Arts%20in%20Film.pdf" || echo "FAILED: Film"

# Food Technology
curl -fSL -o "Food_Technology.pdf" "https://our.upd.edu.ph/files/Checklist/UG/CHE/CHE_Bachelor%20of%20Science%20in%20Food%20Technology.pdf" || echo "FAILED: Food Technology"

# Geodetic Engineering
curl -fSL -o "Geodetic_Engineering.pdf" "https://our.upd.edu.ph/files/Checklist/UG/COE/COE_Bachelor%20of%20Science%20in%20Geodetic%20Engineering.pdf" || echo "FAILED: Geodetic Engineering"

# Geography
curl -fSL -o "Geography.pdf" "https://our.upd.edu.ph/files/Checklist/UG/CSSP/CSSP_Bachelor%20of%20Science%20%28Geography%29.pdf" || echo "FAILED: Geography"

# Geology
curl -fSL -o "Geology.pdf" "https://our.upd.edu.ph/files/Checklist/UG/CS/CS_Bachelor%20of%20Science%20in%20Geology.pdf" || echo "FAILED: Geology"

# History
curl -fSL -o "History.pdf" "https://our.upd.edu.ph/files/Checklist/UG/CSSP/CSSP_Bachelor%20of%20Arts%20%28History%29.pdf" || echo "FAILED: History"

# Home Economics
curl -fSL -o "Home_Economics.pdf" "https://our.upd.edu.ph/files/Checklist/UG/CHE/CHE_Bachelor%20of%20Science%20in%20Home%20Economics.pdf" || echo "FAILED: Home Economics"

# Hotel, Restaurant and Institutional Management
curl -fSL -o "Hotel,_Restaurant_and_Institutional_Management.pdf" "https://our.upd.edu.ph/files/Checklist/UG/CHE/CHE_Bachelor%20of%20Science%20in%20Hotel%2C%20Restaurant%20and%20Institution%20Management.pdf" || echo "FAILED: Hotel, Restaurant and Institutional Management"

# Industrial Design
curl -fSL -o "Industrial_Design.pdf" "https://our.upd.edu.ph/files/Checklist/UG/CFA/CFA_Bachelor%20of%20Fine%20Arts%20%28Industrial%20Design%29.pdf" || echo "FAILED: Industrial Design"

# Industrial Engineering
curl -fSL -o "Industrial_Engineering.pdf" "https://our.upd.edu.ph/files/Checklist/UG/COE/COE_Bachelor%20of%20Science%20in%20Industrial%20Engineering.pdf" || echo "FAILED: Industrial Engineering"

# Interior Design
curl -fSL -o "Interior_Design.pdf" "https://our.upd.edu.ph/files/Checklist/UG/CHE/CHE_Bachelor%20of%20Science%20in%20Interior%20Design.pdf" || echo "FAILED: Interior Design"

# Journalism
curl -fSL -o "Journalism.pdf" "https://our.upd.edu.ph/files/Checklist/UG/CMC/CMC_Bachelor%20of%20Arts%20in%20Journalism.pdf" || echo "FAILED: Journalism"

# Juris Doctor
curl -fSL -o "Juris_Doctor.pdf" "https://our.upd.edu.ph/files/Checklist/UG/LAW/LAW_Juris%20Doctor.pdf" || echo "FAILED: Juris Doctor"

# Landscape Architecture
curl -fSL -o "Landscape_Architecture.pdf" "https://our.upd.edu.ph/files/Checklist/UG/CA/CA_Bachelor%20of%20Landscape%20Architecture.pdf" || echo "FAILED: Landscape Architecture"

# Library and Information Studies
curl -fSL -o "Library_and_Information_Studies.pdf" "https://our.upd.edu.ph/files/Checklist/UG/SLIS/SLIS_Bachelor%20of%20Library%20and%20Information%20Science.pdf" || echo "FAILED: Library and Information Studies"

# Linguistics
curl -fSL -o "Linguistics.pdf" "https://our.upd.edu.ph/files/Checklist/UG/CSSP/CSSP_Bachelor%20of%20Arts%20%28Linguistics%29.pdf" || echo "FAILED: Linguistics"

# Malikhaing Pagsulat
curl -fSL -o "Malikhaing_Pagsulat.pdf" "https://our.upd.edu.ph/files/Checklist/UG/CAL/CAL_Bachelor%20of%20Arts%20%28Malikhaing%20Pagsulat%20sa%20Filipino%29.pdf" || echo "FAILED: Malikhaing Pagsulat"

# Materials Engineering
curl -fSL -o "Materials_Engineering.pdf" "https://our.upd.edu.ph/files/Checklist/UG/COE/COE_Bachelor%20of%20Science%20in%20Materials%20Engineering.pdf" || echo "FAILED: Materials Engineering"

# Mechanical Engineering
curl -fSL -o "Mechanical_Engineering.pdf" "https://our.upd.edu.ph/files/Checklist/UG/COE/COE_Bachelor%20of%20Science%20in%20Mechanical%20Engineering.pdf" || echo "FAILED: Mechanical Engineering"

# Mathematics
curl -fSL -o "Mathematics.pdf" "https://our.upd.edu.ph/files/Checklist/UG/CS/CS_Bachelor%20of%20Science%20in%20Mathematics.pdf" || echo "FAILED: Mathematics"

# Metallurgical Engineering
curl -fSL -o "Metallurgical_Engineering.pdf" "https://our.upd.edu.ph/files/Checklist/UG/COE/COE_Bachelor%20of%20Science%20in%20Metallurgical%20Engineering.pdf" || echo "FAILED: Metallurgical Engineering"

# Mining Engineering
curl -fSL -o "Mining_Engineering.pdf" "https://our.upd.edu.ph/files/Checklist/UG/COE/COE_Bachelor%20of%20Science%20in%20Mining%20Engineering.pdf" || echo "FAILED: Mining Engineering"

# Molecular Biology and Biotechnology
curl -fSL -o "Molecular_Biology_and_Biotechnology.pdf" "https://our.upd.edu.ph/files/Checklist/UG/CS/CS_Bachelor%20of%20Science%20in%20Molecular%20Biology%20and%20Biotechnology.pdf" || echo "FAILED: Molecular Biology and Biotechnology"

# Music
curl -fSL -o "Music.pdf" "https://our.upd.edu.ph/files/Checklist/UG/CM/CM_Bachelor%20of%20Music.pdf" || echo "FAILED: Music"

# Painting
curl -fSL -o "Painting.pdf" "https://our.upd.edu.ph/files/Checklist/UG/CFA/CFA_Bachelor%20of%20Fine%20Arts%20%28Painting%29.pdf" || echo "FAILED: Painting"

# Philippine Studies
curl -fSL -o "Philippine_Studies.pdf" "https://our.upd.edu.ph/files/Checklist/UG/CAL/CAL_Bachelor%20of%20Arts%20%28Philippine%20Studies%29.pdf" || echo "FAILED: Philippine Studies"

# Philosophy
curl -fSL -o "Philosophy.pdf" "https://our.upd.edu.ph/files/Checklist/UG/CSSP/CSSP_Bachelor%20of%20Arts%20%28Philosophy%29.pdf" || echo "FAILED: Philosophy"

# Physical Education
curl -fSL -o "Physical_Education.pdf" "https://our.upd.edu.ph/files/Checklist/UG/CHK/CHK_Bachelor%20of%20Physical%20Education.pdf" || echo "FAILED: Physical Education"

# Physics
curl -fSL -o "Physics.pdf" "https://our.upd.edu.ph/files/Checklist/UG/CS/CS_Bachelor%20of%20Science%20in%20Physics.pdf" || echo "FAILED: Physics"

# Political Science
curl -fSL -o "Political_Science.pdf" "https://our.upd.edu.ph/files/Checklist/UG/CSSP/CSSP_Bachelor%20of%20Arts%20%28Political%20Science%29.pdf" || echo "FAILED: Political Science"

# Psychology
curl -fSL -o "Psychology.pdf" "https://our.upd.edu.ph/files/Checklist/UG/CSSP/CSSP_Bachelor%20of%20Arts%20%28Psychology%29.pdf" || echo "FAILED: Psychology"

# Public Administration
curl -fSL -o "Public_Administration.pdf" "https://our.upd.edu.ph/files/Checklist/UG/NCPAG/NCPAG_Bachelor%20of%20Public%20Administration.pdf" || echo "FAILED: Public Administration"

# Sculpture
curl -fSL -o "Sculpture.pdf" "https://our.upd.edu.ph/files/Checklist/UG/CFA/CFA_Bachelor%20of%20Fine%20Arts%20%28Sculpture%29.pdf" || echo "FAILED: Sculpture"

# Secondary Education
curl -fSL -o "Secondary_Education.pdf" "https://our.upd.edu.ph/files/Checklist/UG/EDUC/EDUC_Bachelor%20of%20Secondary%20Education.pdf" || echo "FAILED: Secondary Education"

# Social Work
curl -fSL -o "Social_Work.pdf" "https://our.upd.edu.ph/files/Checklist/UG/CSWCD/CSWCD_Bachelor%20of%20Science%20in%20Social%20Work.pdf" || echo "FAILED: Social Work"

# Sociology
curl -fSL -o "Sociology.pdf" "https://our.upd.edu.ph/files/Checklist/UG/CSSP/CSSP_Bachelor%20of%20Arts%20%28Sociology%29.pdf" || echo "FAILED: Sociology"

# Speech Communication
curl -fSL -o "Speech_Communication.pdf" "https://our.upd.edu.ph/files/Checklist/UG/CAL/CAL_Bachelor%20of%20Arts%20%28Speech%20Communication%29.pdf" || echo "FAILED: Speech Communication"

# Sport Science
curl -fSL -o "Sport_Science.pdf" "https://our.upd.edu.ph/files/Checklist/UG/CHK/CHK_Bachelor%20of%20Sports%20Science.pdf" || echo "FAILED: Sport Science"

# Sports Studies
curl -fSL -o "Sports_Studies.pdf" "https://our.upd.edu.ph/files/Checklist/UG/CHK/CHK_Certificate%20in%20Sports%20Studies.pdf" || echo "FAILED: Sports Studies"

# Statistics
curl -fSL -o "Statistics.pdf" "https://our.upd.edu.ph/files/Checklist/UG/STAT/STAT_Bachelor%20of%20Science%20%28Statistics%29.pdf" || echo "FAILED: Statistics"

# Theatre Arts
curl -fSL -o "Theatre_Arts.pdf" "https://our.upd.edu.ph/files/Checklist/UG/CAL/CAL_Bachelor%20of%20Arts%20%28Theatre%20Arts%29.pdf" || echo "FAILED: Theatre Arts"

# Tourism
curl -fSL -o "Tourism.pdf" "https://our.upd.edu.ph/files/Checklist/UG/AIT/AIT_Bachelor%20of%20Science%20in%20Tourism.pdf" || echo "FAILED: Tourism"

# Visual Communication
curl -fSL -o "Visual_Communication.pdf" "https://our.upd.edu.ph/files/Checklist/UG/CFA/CFA_Bachelor%20of%20Fine%20Arts%20%28Visual%20Communication%29.pdf" || echo "FAILED: Visual Communication"

