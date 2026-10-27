# AI Use-Case Risk Assessment Questionnaire

Complete one questionnaire per AI use case before it is piloted, purchased, or launched. It takes about 15 minutes. Answer the questions about the system as it will actually be used, not as the vendor describes it.

> Educational template, not legal advice. The `id` column matches the keys in `tools/classify.py`, so your answers can be run through the screening script. The result is a **preliminary** flag for human review.

## Part 1. About the use case

| Field | Your answer |
|---|---|
| Use case name | |
| Business owner | |
| Technical owner | |
| One-sentence purpose | |
| Build, buy, or embed a third-party model? | |
| Vendor and underlying model (if any) | |
| Our role under the EU AI Act | Provider / Deployer / Both / Not sure |
| Will the system or its output be used in the EU? | Yes / No / Unsure |
| Stage | Idea / Pilot / Production |

## Part 2. Prohibited-practice screen

If you answer **yes** to any of these, stop and escalate to Legal before doing anything else.

| id | Question |
|---|---|
| `p_manipulation` | Does the system use subliminal, manipulative, or deceptive techniques that materially distort people's behavior in a way likely to cause significant harm? |
| `p_vulnerability` | Does it exploit vulnerabilities due to a person's age, disability, or social or economic situation to distort behavior in a harmful way? |
| `p_social_scoring` | Does it score or classify people based on their social behavior or personal traits in a way that leads to unjustified or detrimental treatment? |
| `p_crime_prediction` | Does it assess the risk of an individual committing a crime based solely on profiling or personality traits? |
| `p_face_scraping` | Does it build or expand facial-recognition databases by untargeted scraping of images from the internet or CCTV? |
| `p_emotion_work_edu` | Does it infer people's emotions in a workplace or educational setting (other than for medical or safety reasons)? |
| `p_biometric_sensitive` | Does it categorise people by biometric data to infer race, political opinions, union membership, religion, sex life, or sexual orientation? |
| `p_realtime_rbi` | Does it perform real-time remote biometric identification in publicly accessible spaces for law enforcement? |
| `p_intimate_imagery` | Can it generate realistic non-consensual intimate imagery of real people? (New prohibition from 2 December 2026.) |
| `p_csam` | Can it generate child sexual abuse material? (New prohibition from 2 December 2026.) |

## Part 3. High-risk screen

| id | Question |
|---|---|
| `h_annex1_safety` | Is the system a safety component of a product, or itself a product, covered by EU product-safety legislation listed in Annex I (for example machinery, toys, medical devices, vehicles) that requires third-party conformity assessment? |
| `h_biometrics` | Does it perform remote biometric identification, biometric categorisation, or emotion recognition (outside the prohibited cases above)? |
| `h_critical_infrastructure` | Is it a safety component in the management or operation of critical infrastructure (digital infrastructure, road traffic, water, gas, heating, electricity)? |
| `h_education` | Does it determine access or admission to education, evaluate learning outcomes, assess education level, or monitor cheating in tests? |
| `h_employment` | Is it used for recruitment or selection, job advertising targeting, decisions on promotion or termination, task allocation based on behavior or traits, or monitoring and evaluating worker performance? |
| `h_essential_services` | Does it evaluate eligibility for public benefits or services, assess creditworthiness or set credit scores of individuals, price life or health insurance, or prioritise emergency calls or dispatch? |
| `h_law_enforcement` | Is it used by or for law enforcement (for example risk assessments, evidence reliability, or profiling in investigations)? |
| `h_migration` | Is it used in migration, asylum, or border control management? |
| `h_justice_democracy` | Is it used to assist the administration of justice, or to influence elections or voting behavior? |
| `profiling_of_persons` | Does the system profile natural persons (automated processing of personal data to evaluate aspects of a person such as performance, economic situation, preferences, behavior, or location)? |
| `narrow_task_exemption` | **Only answer if you ticked an Annex III area above.** Is the system limited to a narrow procedural task, improving the result of a previously completed human activity, detecting patterns without replacing or influencing human assessment, or doing a preparatory task? |

Note: profiling of natural persons in an Annex III area is always treated as high-risk. The narrow-task exemption cannot be used in that case. If you rely on the exemption, document your reasoning.

## Part 4. Transparency screen

| id | Question |
|---|---|
| `t_interacts_with_people` | Does the system interact directly with people (for example a chatbot or voice assistant) where it might not be obvious they are dealing with AI? |
| `t_synthetic_content` | Does it generate synthetic audio, image, video, or text content? |
| `t_emotion_or_biometric_cat` | Do we deploy an emotion-recognition or biometric-categorisation system whose output affects people exposed to it? |
| `t_deepfake` | Does it generate or manipulate image, audio, or video that resembles real people, places, or events and could appear authentic? |
| `t_public_interest_text` | Does it generate or manipulate text published to inform the public on matters of public interest, without human editorial review? |

## Part 5. General-purpose AI model screen

| id | Question |
|---|---|
| `gpai_provider` | Are we the **provider** of a general-purpose AI model (one trained on broad data, with significant generality, that can perform a wide range of tasks)? Answer no if we only use someone else's model. |
| `gpai_systemic_risk` | If yes above: is the model trained with more than 10^25 floating-point operations, or has it been designated as a model with systemic risk? |

## Part 6. Data and impact (for governance, not tier classification)

| Question | Your answer |
|---|---|
| Does the system process personal data? Which categories? | |
| Special-category data (health, biometrics, etc.)? | |
| Who is affected: customers, employees, the public, children? | |
| Can the system's output materially affect someone's rights, pay, access, or opportunities? | |
| What is the human-oversight design (who can review, override, or stop it)? | |
| How will accuracy, bias, and drift be tested and monitored? | |
| Is a data protection impact assessment (DPIA) needed or complete? | |
| Which third parties receive our data or provide the model? | |
| What happens if the system fails or gives a wrong answer? | |

## Part 7. Review and sign-off

| Role | Name | Decision | Date |
|---|---|---|---|
| Business owner | | | |
| Technical owner | | | |
| Legal / Privacy | | | |
| Risk / Compliance | | | |
| AI governance committee (if tier is high-risk or above) | | | |

**Final tier (human-determined):** ____________________

**Conditions of approval and review date:** ____________________
