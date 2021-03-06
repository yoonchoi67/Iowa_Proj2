# Iowa_Proj2

**EVERYONE GIVE ME FEEDBACKS ON MY CODE BEFORE TUESDAY OR I WILL ASSUME THAT YOU GUYS LOOKED OVER THEM AND AGREE WITH ME.**


## **METHODS**
(we will put the below on the 'PRESENT METHODS' section)
### **General Steps**
[x] Change all medication XML tags to CSV in lower case and put them in our_code/medication.csv.

[x] Loop through the data in CSV from our_code/analysis_refactored.py iteratively.

[x] Understand that the data (or each row) in medication.csv can be divided into two big categories: 
1. row where medication_id starts with 'DOC'
2. row where medication_id starts with 'M'

    The one with 'DOC' is the big tag that encloses the others with 'M' until the next 'DOC' comes up. The answers to the questions differ based on how we interpret this.

[x] Understand that analysis_data2 is the data that I am describing below but I have left analysis_data as is in case we need them for future reference. The latest code used for analysis_data is commit 31.

### **Question 2a:**
[x] Frequency distribution of the medications taken

1. This method returns a list of tuples where first element of the tuple is a medication name and the second element is a frequency of the medication.
2. We loop through only the rows that fit the second category (starts with 'M') in medication.csv. This is because the ones from the first category does not have the 'text' field that indicates the medications.
3. We utilize the list 'intermerdiate_medicines' to store 'text' field from each row in the second category until the next row's medication_id starts with 'DOC' (first category), which then we will flush out the elements in the list. This means that this method doesn't double-count the medication if they are the same name and under the same first category, but does not prevent from double-counting if they are from different first category.
    - This means double-counting of the same medications is possible even if the only difference between the first category is the time. However, we left it as is because time is an important aspect of the medication frequency due to the possibility of getting on/off the drugs from before/during/after the DCT.

### **Question 2b:**
[x] Frequency distribution of categories of medications taken

1. This method returns a list of tuples where first element of the tuple is a medication category and the second element is a frequency of the medication category.
2. We loop through only the rows that fit the first category (starts with 'DOC') in medication.csv. This is because the ones from the first category encompasses the ones from the second category that follows after.
3. We store the 'type1' and 'type2' field from each row without regard to which type it is. We disregarded the different types and simply aggregated them because the medicines with two types still mean that the medicines are witihin the bounds of these two and we cannot ignore one another and doesn't mean the first type is more important than the second type. We also safely skipped over the second category because the first category rows encompasses the second category rows that follow.

### **Question 3 and 4:**
[x] 10 individuals taking the greatest/least number of medication types

1. This method returns a list of tuples where first element of the tuple is a patient id and the second element is a frequency of the medication types for the said patient.
2. Similarly with question 2b, we loop through only the rows that fit the first category (starts with 'DOC') in medication.csv. This is because the ones from the first category encompasses the ones from the second category that follows after.
3. For each patient, we aggregate the type1 and type2 field of the rows as long as we haven't counted the medication type inside the patient's medication type taken.
4. After we gathered all the medication types from a patient, we simply count the number of them and thus we get our result.

### **Question 5:**
[x] Frequency distribution of the medications taken

1. This method returns a list of tuples where first element of the tuple is a patient id and the second element is a frequency of the medication for the said patient.
2. We loop through only the rows that fit the second category (starts with 'M') in medication.csv. This is because the ones from the first category does not have the 'text' field that indicates the medications.
3. Similarly with question 2a, we utilize the list 'intermerdiate_medicines' to store 'text' field from each row in the second category until the next row's medication_id starts with 'DOC' (first category), which then we will flush out the elements in the list. This means that this method doesn't double-count the medication if they are the same name and under the same first category, but does not prevent from double-counting if they are from different first category.
    - This means double-counting of the same medications is possible even if the only difference between the first category is the time. However, we left it as is because time is an important aspect of the medication frequency due to the possibility of getting on/off the drugs from before/during/after the DCT.
4. Then, similarly with question 4, after we have gathered all the medication names from a patient, we simply count the number of them and thus we get our result.

## **RESULTS**
Results available in the Project_Paper.docx.

## **LIMITATIONS**
(we will put the below on the 'LIMITATIONS' section)

1. Double-counting of the same medications is possible for the frequency questions even if the only difference between the medications is the time. This is due to the fact that tags whose medication_id starts with 'DOC' differ from one another only by the 'time' field while medication tags inside are identical. However, we must see this not only as limitations, but also by design, because time is an important aspect of the medication frequency due to the possibility of getting on/off the drugs from before/during/after the DCT.

2. We constructed the frequency results based on their relevant strings, so if the 'text' field had any discrepancies from the representatives due to spelling errors or long strings, the medicine didn't match well enough to contribute to the frequency. For example, we couldn't make sense of 'dilt (30mg TID)' from 114-04.xml so we left them out. This could mean that we were missing some relevant medicines. However, our dataset was large enough to justify filtering through the anomalies and we are confident that we had enough data to make a proper analysis. 

## CONCLUSION
(we will put the below on the 'CONCLUSION' section)

1. There are various information available through patient clinical notes dataset that we can use for health data analysis. 