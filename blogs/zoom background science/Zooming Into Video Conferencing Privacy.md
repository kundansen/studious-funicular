# Zooming Into Video Conferencing Privacy
**Authors:** Dima Kagan, Galit Fuhrmann Alpert, and Michael Fire  
**Publication Date:** February 2024

---

## Abstract

- **Focus:** Examination of privacy and security risks in video conferencing.
- **Data:** Analysis of over 15,000 publicly posted collage images (with 142,000+ face images).
- **Findings:** Personal data (e.g., age, gender, usernames, full names) can be easily extracted; cross-referencing this data can enable linkage attacks that jeopardize both online and offline security.

---

## I. Introduction

- **Context:** COVID-19 led to a surge in video conferencing (e.g., Zoom, Teams, Google Meet) affecting millions daily.
- **Privacy Concerns:**
  - Meeting images inadvertently reveal personal details.
  - Data leakage includes face images, age, gender, and user identities.
  - Malicious users could use deepfake tools to impersonate others.
- **Aim:** To provide an in-depth analysis of privacy issues by mining publicly posted video conference images and demonstrating how extracted data can be linked to reveal personal information.

---

## II. Background

- **Prior Work:** Reviews privacy issues on social networks, IoT, and online platforms.
- **Unique Risks:** 
  - Video conference images have a fixed structure with embedded usernames.
  - These characteristics make them more vulnerable to data extraction and linkage attacks.

---

## III. Methods

### A. Building a Database of Video Conference Images
- **Data Collection:**  
  - Web crawlers were deployed on Twitter and Instagram using specific hashtags (e.g., “#zoommeeting”).
  - Over 15,000 Zoom collage images were collected.
- **Image Filtering:**  
  - Duplicate and similar images were removed using perceptual hashing (dhash) and image embedding comparisons.

### B. Automatically Extracting Private Information
- **Face Detection & Embedding:**  
  - Two tools were used (an MTCNN-based model and Microsoft Azure Face API) to detect faces and generate 128-dimensional vectors.
- **Age & Gender Detection:**  
  - Pretrained models and Azure API were used to estimate age and determine gender.
- **Username Recognition:**  
  - A scene text recognition library (based on EAST and MORAN) with custom heuristics merged adjacent words to extract usernames, achieving ~63.4% accuracy.

### C. Linking Personal User Data to Social Network Data
- **Linkage Approach:**  
  - Matched usernames and face embeddings across meeting images.
  - Constructed a social network graph where nodes represent meeting participants and edges represent co-participation.
- **Validation:**  
  - Manual comparison with social media profiles verified identity matches.

### D. Linkage by Background
- **Background Analysis:**  
  - Utilized object detection (Faster R-CNN) to segment individual user blocks (face + background).
  - Compared background blocks using image features to link users across different meetings.

---

## IV. Results

- **Dataset Overview:**
  - 15,783 Zoom collage images and 142,001 face images analyzed.
  - Participants' average estimated age is ~29; gender detection identified tens of thousands of male and female faces.
- **Username Findings:**
  - Extracted 85,616 different usernames; over 57% consisted of multiple words, indicating more disclosive details.
- **Social Network Graph:**
  - Constructed a graph with 16,842 nodes and nearly 200,000 edges; the largest connected component contained over 3,000 nodes.
- **Linkage Attacks:**
  - Cross-referencing usernames and facial embeddings can match participants to social media profiles.
  - Simulations indicate that even partial privacy measures (e.g., 20% of users protecting themselves) can reduce network link density by ~36%.
- **Background Linkage:**
  - In 96% of inspected pairs, participants used the same or slightly modified backgrounds, which can be used to track individuals across meetings.

---

## V. Discussion

- **Multiparty Privacy Challenges:**
  - Video conference images leak personal data (e.g., embedded usernames), making multiparty privacy (MP) difficult to manage.
- **Ease of Data Collection:**
  - Publicly available images on social media make it simple for attackers to harvest and aggregate personal data.
- **Privacy Risks Across Demographics:**
  - Risks affect all age groups, including vulnerable populations like children and older adults.
- **Organizational Risks:**
  - Data leakage from employee meetings can compromise organizational security by revealing internal social networks.
- **Linkage Attacks:**
  - Aggregating data from multiple meetings can expose extended social networks, further jeopardizing privacy.

---

## VI. Recommendations for Privacy Protection

1. **Use Voice-Only Options:**  
   - Avoid unnecessary video streaming; use hardware controls (e.g., microphone on/off buttons) to protect audio privacy.
2. **Generic Pseudonyms:**  
   - Use non-identifiable, generic usernames to reduce cross-referencing risks.
3. **Generic Virtual Backgrounds:**  
   - Use non-distinctive, generic backgrounds to avoid revealing personal environment details.
4. **Anti-Facial Recognition Measures:**  
   - Consider accessories or filters (e.g., masks or noise filters) to disrupt facial recognition.
5. **Organizational Policies:**  
   - Update organizational policies to limit what can be shared during video conferences.
6. **Monitor Children’s Activity:**  
   - Parents and educators should actively monitor and adjust privacy settings for children.
7. **Privacy Mode in Conferencing Tools:**  
   - Implement privacy modes (e.g., notifications for screenshots) in video conferencing software.
8. **Tighten Social Media Privacy Settings:**  
   - Adjust privacy settings on social networks to restrict access to meeting images.

---

## VII. Summary and Conclusion

- **Key Findings:**  
  - Publicly posted video conference images leak significant personal information.
  - It is possible to construct large social networks and perform linkage attacks using publicly available data.
- **Implications:**  
  - Video conferencing privacy poses a critical threat to both individual and organizational security.
  - Even partial privacy measures may not suffice against sophisticated data aggregation attacks.
- **Call to Action:**  
  - Users and organizations must adopt robust privacy practices.
  - Video conferencing platforms need to implement better background separation algorithms and enhanced privacy modes.


## Key Information on Video Conferencing Backgrounds and Their Impact on Privacy

### Overview
- **Objective:**  
  The paper examines the privacy and security threats inherent in video conferencing platforms, focusing on how meeting images (such as Zoom collages) can leak sensitive personal information.
- **Dataset and Methods:**  
  The study curated a dataset of over 15,000 publicly posted Zoom collage images (containing 142,000 face images) from social media platforms and applied deep-learning–based image processing techniques to extract information such as age, gender, and usernames.

### Virtual Backgrounds and Information Leakage
- **Glitches in Virtual Backgrounds:**  
  Although virtual backgrounds are designed to hide personal environments, glitches in the image matting process can reveal fragments of the actual background.
  - **Quote:**  
    > "Apparently, these artifacts contain information about the physical environment and expose real-world pixels."
- **Risk of Data Leakage:**  
  The leaked background data can include unique identifiers that not only reveal details about the user's physical environment but also enable attackers to link a user's identity across multiple meetings.

### Linking Personal Data via Backgrounds
- **Linkage by Background:**  
  The paper details how even minor modifications (e.g., filter changes) do little to prevent attackers from clustering similar backgrounds and linking them to the same user.
  - **Quote:**  
    > "We demonstrated that even the user’s background could be used to connect between different meetings and people."
- **Social Network Reconstruction:**  
  By cross-referencing face embeddings and extracted usernames, the study constructs social networks of meeting participants—illustrating how private data can be aggregated from multiple sources.

### Privacy Risks and Broader Implications
- **Vulnerability Across Age Groups:**  
  The dataset shows that participants range from children to older adults, highlighting that privacy risks affect a wide demographic.
- **Organizational and Individual Threats:**  
  The leakage of background information poses threats not only to individual privacy but also to organizational security, as aggregated data can expose internal networks and social ties.

### Recommendations for Mitigation
- **Improving Virtual Backgrounds:**  
  The authors suggest that better matting algorithms could reduce the leakage of private background details.
- **User Practices:**  
  Users are advised to employ generic backgrounds, use pseudonyms, and consider privacy-enhancing accessories (e.g., anti-facial recognition filters) to mitigate risks.
- **Organizational Policies:**  
  Organizations should update policies regarding what can be shared in video conferences and educate employees on privacy risks and best practices.

### Summary
- **Core Finding:**  
  Virtual backgrounds, while intended to protect user privacy, may inadvertently leak enough information to compromise both individual and organizational privacy.
- **Implication:**  
  Enhanced security measures and improved background processing technologies are essential to safeguard sensitive information in the era of widespread video conferencing.
```

