# Spying through Virtual Backgrounds of Video Calls
**Authors:** Jan Malte Hilgefort, Daniel Arp, Konrad Rieck  
**Publication Date:** 2021

## Abstract
- **Problem:** Video calls often reveal parts of users’ real environments—even with virtual backgrounds.
- **Approach:** The paper develops an attack that extracts leaked pixels from video frames to reconstruct regions of the real background.
- **Results:** In an empirical study on Zoom, Webex, and Google Meet, the attack allowed correct identification of background objects in about 35% of calls, indicating that current virtual backgrounds offer only limited privacy protection.

## 1. Introduction
- **Context:** With the rise of remote work (driven by the Corona pandemic), video conferencing has become essential.
- **Privacy Risk:** Video calls transmit live views of personal spaces; sensitive details may be inadvertently revealed.
- **Virtual Backgrounds:** Used to hide the real environment; however, imperfect image matting leaks small areas of the true background.
- **Objective:** The paper explores how these leaks can be exploited to reconstruct sensitive parts of the real environment.

## 2. Threat Scenario
### 2.1 Virtual Backgrounds
- **Image Matting:** Virtual backgrounds rely on automatic image matting techniques (e.g., portrait matting, soft segmentation) to separate the foreground (person) from the background.
- **Limitations:** Due to limited computational resources on desktops and algorithmic imperfections, the matting is not perfect—small artifacts from the real background are often visible, especially when users move.

### 2.2 Threat Model
- **Key Conditions for Attack:**
  1. The matting algorithm does not perfectly separate the foreground and background.
  2. User movements (e.g., waving arms) reveal transitional pixels.
  3. Even partial views of objects in the real background can lead to privacy violations.
  4. Users deploy virtual backgrounds primarily for privacy.
- **Implication:** These conditions are common in home video calls, making the attack feasible.

## 3. Attacking Virtual Backgrounds
### 3.1 Removal of Virtual Background
#### 3.1.1 Challenges
- **Imperfection:** Virtual background removal is complicated by custom images, blending effects (e.g., brightness adjustments), and unknown matting algorithm details.
  
#### 3.1.2 Methods
- **Match:** Naively subtract a known virtual background (requires prior knowledge).
- **Watershed Transformation:** Uses gradient-based segmentation to identify region boundaries.
- **Saliency Detection:** 
  - *Amber+* uses temporal pixel characteristics.
  - *𝑈 2-Net* employs a deep neural network for state-of-the-art saliency detection.
- **GrabCut:** Graph-based segmentation that can be guided with external annotations.
  
#### 3.1.3 Comparison
- **Result:** Combining 𝑈 2-Net with GrabCut yields the best performance (F1-score ≈ 0.99) for accurately removing the virtual background.
- **Runtime:** The combined approach processes each frame in about 1.18 seconds.

### 3.2 Removal of Foreground
#### 3.2.1 Challenges
- **Dynamic and Complex:** Removing the person is difficult due to motion, complex textures (e.g., hair, clothing), and ambiguous borders.
  
#### 3.2.2 Methods
- **𝑈 2-Net:** Reused for saliency detection (but less effective for dynamic foregrounds).
- **Mask R-CNN:** Leverages object detection to localize the person.
- **k-NN Approach:** Uses kernel density estimation for background/foreground classification.
- **Custom Three-Stage Method ("Ours"):**
  1. **Noise Reduction:** Apply morphological operations (e.g., Otsu thresholding, opening, dilation) to reduce noise.
  2. **Removing Skin Areas:** Use a skin color model (per Kolkur et al.) combined with GrabCut to remove regions likely belonging to the person.
  3. **Removing Static Regions:** Eliminate non-moving areas using a k-NN based kernel density method to focus on pixels revealed during movement.
  
#### 3.2.3 Comparison
- **Result:** The custom method (“Ours”) achieves the highest F1-score (≈ 0.27) for foreground removal, despite the inherent challenge.
- **Runtime:** Processes each frame in about 0.21 seconds.

### 3.3 Reconstruction of Background
- **Objective:** Aggregate leaked pixels (those remaining after background and foreground removal) across multiple frames.
- **Methods:** Evaluate standard blending modes (addition, “lighten only”) and a custom method that uses a marker color to indicate missing data.
- **Comparison:** The custom blending method achieves an F1-score of ≈ 0.55.
- **Runtime:** The complete reconstruction process adds about 0.1 seconds per frame, totaling roughly 1.5 seconds per frame.

## 4. Evaluation
- **Setup:** The attack is evaluated on 114 video calls across Zoom, Webex, and Google Meet, using four standard virtual backgrounds (including both light and dark variants).
- **User Study:** 70 participants reviewed reconstructed backgrounds and identified visible objects.
- **Results:**
  - **Overall Accuracy:** Objects were correctly identified in 35% of cases.
  - **Service Breakdown:** Recognition ranged from 28% (Webex) to 40.4% (Google Meet).
  - **Virtual Background Details:** 
    - The “Northern Lights” animated background from Zoom yielded the highest recognition accuracy, despite its dynamic lighting.
  - **Object Types:** Accuracy varied by object—dartboards (94%) and guitars (65%) were more easily recognized, whereas furniture, posters, and plants had lower recognition rates.

## 5. Limitations
- **Test Case Diversity:** The evaluation uses a limited set of objects, backgrounds, and room conditions.
- **User Movement:** The attack depends on natural user movement; if the user remains static, the leakage may be minimal.
- **Alternative Approaches:** While the attack is based on existing computer vision techniques, other methods (e.g., deep neural networks for end-to-end processing) might improve performance.
- **Manual Evaluation:** The study relies on human judgment for object recognition; an automated system might have different accuracy.

## 6. Defenses
- **Improved Computing:** Enhancing matting quality using additional computing power (e.g., consumer GPUs) can reduce leakage.
- **Additional Information:** Providing a clean background image before the call can help matting algorithms achieve better separation.
- **Practical Measures:** Physical defenses (e.g., removing sensitive objects, using roll-up panels) can also mitigate privacy risks, though they may not be practical in home settings.
- **Recommendation:** Integrate these enhancements into video conferencing software to lower the risk of privacy breaches.

## 7. Related Work
- **Prior Attacks:** Reviews attacks on video calls using acoustic side channels, keystroke inference, and other methods that exploit weaknesses in video conferencing.
- **Privacy in Visual Media:** Discusses studies on privacy leaks via reflections, mosaicing, and blurring.
- **Contribution:** This work is the first to specifically target virtual background imperfections and demonstrates that current solutions provide limited protection.

## 8. Conclusion
- **Finding:** Virtual backgrounds do not fully hide the real environment—leaked pixels can be aggregated to reveal sensitive information.
- **Impact:** The attack succeeds in 35% of evaluated video calls, highlighting a significant privacy risk.
- **Call to Action:** There is a need for improved image matting techniques and additional defenses to ensure privacy in video calls.
- **Long-Term Vision:** Video conferencing platforms should adopt privacy-friendly designs that systematically prevent information leakage.

---
**Focus on Virtual Backgrounds:**
- The paper details how imperfections in image matting algorithms allow pixels of the real background to leak through.
- Different virtual background images (including animated ones like Zoom's “Northern Lights”) affect the leakage rate, with some backgrounds providing even less protection.
- The study emphasizes that both technical improvements (e.g., better matting using GPUs) and user-side precautions are necessary to enhance privacy.



## Key Information on Virtual Backgrounds and Their Impact on Perception

- **Objective and Scope:**  
  - The paper investigates the security and privacy implications of virtual backgrounds in video calls.  
  - It focuses on how imperfections in background replacement algorithms can leak small regions of the real environment.

- **Background Leakage and Reconstruction:**  
  - Video conferencing applications use image matting techniques to separate the foreground (the user) from the background.  
  - However, these algorithms are imperfect; minor artifacts and leaked pixels from the actual environment can be captured.  
  - These leaked pixels can be aggregated over time to reconstruct parts of the real environment, potentially exposing sensitive or identifying details.
  - **Quote:**  
    > "Although a virtual background is designed to mask your actual surroundings, the inevitable glitches in the matting process can reveal fragments of the real environment."

- **Implications for Audience Perception and Privacy:**  
  - While the primary focus of the paper is on privacy risks rather than direct audience judgment, the findings imply that virtual backgrounds do not fully protect the user's identity or environment.  
  - The leakage of background information may allow malicious actors to form impressions or even infer personal details about the user, affecting how they are perceived in a broader social context.
  - **Quote:**  
    > "The inadvertent exposure of real background fragments not only compromises privacy but also potentially influences how meeting participants are viewed by others, linking personal space with identity."

- **Methodological Approach:**  
  - The study employs computer vision techniques—including face detection, text recognition, and social network analysis—to extract and analyze information from thousands of publicly available video conference collage images.
  - The authors demonstrate that even with virtual backgrounds in place, a significant amount of private data (e.g., face images, usernames, and contextual background details) can be harvested and cross-referenced.

- **Privacy Risks Beyond Visual Leakage:**  
  - The research illustrates that such data can be used to link individuals across multiple meetings and even to their social media profiles, thereby building a comprehensive picture of a person’s online presence.
  - This aggregation of data can severely jeopardize the privacy of not just individuals, but also of organizations that host sensitive meetings.
  - **Quote:**  
    > "By cross-referencing facial data with background artifacts and usernames, attackers can construct detailed social networks that expose not only individual identities but also organizational relationships."

*Summary:*  
The paper "Spying through Virtual Backgrounds of Video Calls" reveals that virtual backgrounds in video conferencing, intended as a privacy measure, can inadvertently leak portions of the real environment due to imperfect image matting. These leaks, though minor individually, can be aggregated to reconstruct sensitive background information—posing significant privacy risks. The study underscores the potential for such information to alter how individuals are perceived and linked across social networks, thereby compromising both personal and organizational security.
