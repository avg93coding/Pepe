<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Early Lung Cancer Detection: A Primary Care Imperative</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', sans-serif;
            background-color: #F0F9FF; /* Lightest blue from a vibrant blue palette */
        }
        .chart-container {
            position: relative;
            width: 100%;
            max-width: 600px; /* Default max-width */
            margin-left: auto;
            margin-right: auto;
            height: 300px; /* Base height */
            max-height: 400px; /* Max height */
        }
        @media (min-width: 768px) { /* md breakpoint */
            .chart-container {
                height: 350px;
            }
        }
        @media (min-width: 1024px) { /* lg breakpoint */
            .chart-container {
                height: 400px;
            }
        }
        .stat-card {
            background-color: #CAF0F8; /* Light blue accent */
            border-left: 5px solid #0077B6; /* Primary blue */
        }
        .section-title {
            color: #005A8D; /* Darker primary blue */
        }
        .flowchart-step {
            border: 2px solid #00B4D8; /* Secondary blue */
            background-color: white;
            color: #005A8D;
        }
        .flowchart-arrow {
            color: #0077B6; /* Primary blue */
        }
        .red-flag {
            color: #D90429; /* A contrasting red for emphasis */
            font-weight: 600;
        }
        .subtle-symptom {
            color: #0077B6; /* Primary blue */
        }
        .guideline-box {
            border: 1px solid #ADE8F4; /* Accent blue */
            background-color: #E0FBFC;
        }
        .tab {
            cursor: pointer;
            padding: 0.75rem 1.5rem;
            margin-right: 0.5rem;
            border-radius: 0.5rem 0.5rem 0 0;
            background-color: #E0E7FF; /* Light Indigo for inactive tabs */
            color: #3730A3; /* Indigo for inactive tab text */
            font-weight: 500;
        }
        .tab.active {
            background-color: #0077B6; /* Primary blue for active tab */
            color: white;
        }
        .tab-content {
            display: none;
            padding: 1.5rem;
            border: 1px solid #0077B6;
            border-top: none;
            border-radius: 0 0 0.5rem 0.5rem;
            background-color: white;
        }
        .tab-content.active {
            display: block;
        }
    </style>
</head>
<body class="antialiased text-gray-800">

    <header class="bg-[#0077B6] text-white py-8 px-4 text-center shadow-lg">
        <h1 class="text-4xl md:text-5xl font-bold mb-2">Early Lung Cancer Detection</h1>
        <p class="text-xl md:text-2xl font-light">A Primary Care Imperative for Improved Outcomes</p>
    </header>

    <main class="container mx-auto px-4 py-8">

        <section id="importance" class="mb-12">
            <h2 class="text-3xl font-semibold mb-6 text-center section-title">The Critical Window: Why Early Detection Saves Lives</h2>
            <p class="text-lg text-gray-700 mb-8 text-center max-w-3xl mx-auto">
                Lung cancer remains a leading cause of cancer-related mortality globally and in Colombia. However, the prognosis dramatically improves when the disease is identified at an early stage. Primary care physicians are at the forefront of this battle, playing a pivotal role in recognizing initial signs, assessing risk, and guiding patients towards timely diagnosis and treatment. This section highlights the stark contrast in survival rates and underscores the urgency of enhancing early detection strategies in the primary care setting.
            </p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
                <div class="bg-white p-6 rounded-lg shadow-xl text-center">
                    <h3 class="text-2xl font-semibold text-[#0077B6] mb-2">Diagnosed Early (Stage I/II)</h3>
                    <p class="text-5xl font-bold text-[#00B4D8] mb-3">60-70%</p>
                    <p class="text-gray-600 text-lg">5-Year Survival Rate</p>
                    <p class="text-sm text-gray-500 mt-2">Significantly better chance of curative treatment.</p>
                </div>
                <div class="bg-white p-6 rounded-lg shadow-xl text-center">
                    <h3 class="text-2xl font-semibold text-[#0077B6] mb-2">Diagnosed Late (Stage IV)</h3>
                    <p class="text-5xl font-bold text-red-500 mb-3">&lt;10%</p>
                    <p class="text-gray-600 text-lg">5-Year Survival Rate</p>
                    <p class="text-sm text-gray-500 mt-2">Limited treatment options, focus often palliative.</p>
                </div>
            </div>
            <div class="bg-white p-6 rounded-lg shadow-xl">
                <h3 class="text-2xl font-semibold text-[#0077B6] mb-4 text-center">Stage at Diagnosis: A Major Determinant</h3>
                 <p class="text-md text-gray-700 mb-4 text-center">
                    Unfortunately, a significant portion of lung cancer cases are still diagnosed at advanced stages when treatment is less effective. The chart below illustrates a typical distribution, emphasizing the need to shift diagnosis towards earlier stages.
                </p>
                <div class="chart-container mx-auto h-[350px] md:h-[400px]">
                    <canvas id="stageAtDiagnosisChart"></canvas>
                </div>
                <p class="text-sm text-gray-600 mt-4 text-center">Data presented is illustrative of typical distributions found in epidemiological studies. Actual percentages can vary by population and region.</p>
            </div>
        </section>

        <section id="epidemiology" class="mb-12">
            <h2 class="text-3xl font-semibold mb-6 text-center section-title">The Global & Colombian Landscape: Understanding the Burden</h2>
            <p class="text-lg text-gray-700 mb-8 text-center max-w-3xl mx-auto">
                Understanding the epidemiology of lung cancer, both globally and within Colombia, is crucial for appreciating the scale of the problem and tailoring public health interventions. Lung cancer consistently ranks among the most common cancers and the leading causes of cancer death worldwide. This section provides an overview of current incidence and mortality statistics.
            </p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div class="bg-white p-6 rounded-lg shadow-xl">
                    <h3 class="text-2xl font-semibold text-[#0077B6] mb-4 text-center">Global Lung Cancer Statistics (Annual Estimates)</h3>
                    <p class="text-md text-gray-700 mb-4 text-center">
                        The following chart compares estimated new cases and deaths globally, highlighting the significant impact of lung cancer.
                    </p>
                    <div class="chart-container mx-auto h-[300px] md:h-[350px]">
                        <canvas id="globalLungCancerStatsChart"></canvas>
                    </div>
                     <p class="text-sm text-gray-600 mt-4 text-center">Estimates based on recent global cancer statistics (e.g., GLOBOCAN).</p>
                </div>
                <div class="bg-white p-6 rounded-lg shadow-xl">
                    <h3 class="text-2xl font-semibold text-[#0077B6] mb-4 text-center">Lung Cancer in Colombia (Annual Estimates)</h3>
                     <p class="text-md text-gray-700 mb-4 text-center">
                        In Colombia, lung cancer also represents a major public health challenge. This chart shows estimated national figures.
                    </p>
                    <div class="chart-container mx-auto h-[300px] md:h-[350px]">
                        <canvas id="colombianLungCancerStatsChart"></canvas>
                    </div>
                    <p class="text-sm text-gray-600 mt-4 text-center">Estimates based on Colombian national cancer registries and health ministry data.</p>
                </div>
            </div>
            <div class="bg-white p-6 rounded-lg shadow-xl mt-8">
                <h3 class="text-2xl font-semibold text-[#0077B6] mb-4 text-center">Lung Cancer as a Proportion of All Cancer Deaths</h3>
                 <p class="text-md text-gray-700 mb-4 text-center">
                    This visualization emphasizes the lethality of lung cancer compared to other malignancies.
                </p>
                <div class="chart-container mx-auto h-[350px] md:h-[400px] max-w-md">
                    <canvas id="lungCancerProportionOfDeathsChart"></canvas>
                </div>
                <p class="text-sm text-gray-600 mt-4 text-center">Illustrative data showing lung cancer's significant contribution to overall cancer mortality.</p>
            </div>
        </section>

        <section id="symptoms" class="mb-12">
            <h2 class="text-3xl font-semibold mb-6 text-center section-title">Recognizing the Warnings: Signs & Symptoms</h2>
            <p class="text-lg text-gray-700 mb-8 text-center max-w-3xl mx-auto">
                Early symptoms of lung cancer can be subtle and often mistaken for less serious conditions. Primary care physicians must maintain a high index of suspicion, especially in at-risk patients. This section outlines common early/subtle symptoms and critical red flags that warrant immediate investigation, referencing guidelines from NCCN and ASCO.
            </p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div class="bg-white p-6 rounded-lg shadow-xl">
                    <h3 class="text-2xl font-semibold text-[#0077B6] mb-4">Early & Subtle Symptoms</h3>
                    <p class="text-gray-600 mb-4">These may be non-specific and require careful evaluation in context of risk factors:</p>
                    <ul class="space-y-2">
                        <li class="flex items-center subtle-symptom"><span class="mr-2 text-xl">🩺</span> Persistent cough (new or changed)</li>
                        <li class="flex items-center subtle-symptom"><span class="mr-2 text-xl">😮‍💨</span> Increasing shortness of breath (dyspnea)</li>
                        <li class="flex items-center subtle-symptom"><span class="mr-2 text-xl">😟</span> Vague, persistent chest, back, or shoulder pain</li>
                        <li class="flex items-center subtle-symptom"><span class="mr-2 text-xl">📉</span> Unexplained weight loss</li>
                        <li class="flex items-center subtle-symptom"><span class="mr-2 text-xl">😩</span> Persistent fatigue or lethargy</li>
                        <li class="flex items-center subtle-symptom"><span class="mr-2 text-xl">🗣️</span> Hoarseness (new or worsening)</li>
                        <li class="flex items-center subtle-symptom"><span class="mr-2 text-xl">🔄</span> Recurrent respiratory infections (e.g., bronchitis, pneumonia)</li>
                    </ul>
                </div>
                <div class="bg-white p-6 rounded-lg shadow-xl">
                    <h3 class="text-2xl font-semibold text-red-600 mb-4">🚨 Red Flag Symptoms 🚨</h3>
                    <p class="text-gray-600 mb-4">These symptoms demand urgent investigation for potential malignancy:</p>
                    <ul class="space-y-2">
                        <li class="flex items-center red-flag"><span class="mr-2 text-xl">🩸</span> Hemoptysis (coughing up blood)</li>
                        <li class="flex items-center red-flag"><span class="mr-2 text-xl">🦴</span> New onset bone pain, especially if persistent or nocturnal</li>
                        <li class="flex items-center red-flag"><span class="mr-2 text-xl">🧠</span> Neurological symptoms (e.g., persistent headache, seizures, weakness, speech changes)</li>
                        <li class="flex items-center red-flag"><span class="mr-2 text-xl"> SVC</span> Superior Vena Cava (SVC) obstruction signs (facial/neck swelling, dyspnea)</li>
                        <li class="flex items-center red-flag"><span class="mr-2 text-xl"> lymph</span> Palpable supraclavicular or cervical lymphadenopathy</li>
                        <li class="flex items-center red-flag"><span class="mr-2 text-xl">🫁</span> Unexplained pleural effusion</li>
                    </ul>
                </div>
            </div>
            <p class="text-md text-gray-600 mt-8 text-center guideline-box p-4 rounded-lg">
                <strong>Clinical Pearl:</strong> According to NCCN and ASCO guidelines, any patient presenting with red flag symptoms, or persistent unexplained symptoms concerning for lung cancer (especially with risk factors), should undergo prompt diagnostic evaluation, typically starting with a chest CT scan if a chest X-ray is unrevealing or suspicious.
            </p>
        </section>

        <section id="risk-factors" class="mb-12">
            <h2 class="text-3xl font-semibold mb-6 text-center section-title">Identifying Vulnerability: Key Risk Factors</h2>
            <p class="text-lg text-gray-700 mb-8 text-center max-w-3xl mx-auto">
                A thorough understanding of lung cancer risk factors is essential for primary care physicians to identify high-risk individuals who may benefit from increased vigilance or screening. Risk factors can be broadly categorized into modifiable and non-modifiable. This section details these factors, drawing upon international guidelines and epidemiological data.
            </p>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div class="bg-white p-6 rounded-lg shadow-xl">
                    <h3 class="text-2xl font-semibold text-[#0077B6] mb-4 text-center">Major Lung Cancer Risk Factors</h3>
                     <p class="text-md text-gray-700 mb-4 text-center">
                        The chart below illustrates the relative impact of common risk factors. Tobacco smoking remains the predominant cause.
                    </p>
                    <div class="chart-container mx-auto h-[400px] md:h-[450px]">
                        <canvas id="riskFactorContributionChart"></canvas>
                    </div>
                </div>
                <div class="bg-white p-6 rounded-lg shadow-xl">
                    <h3 class="text-2xl font-semibold text-[#0077B6] mb-4 text-center">Modifiable vs. Non-Modifiable Risk Factors</h3>
                    <div class="mb-6">
                        <h4 class="text-xl font-medium text-[#00B4D8] mb-2">🚬 Modifiable Risk Factors:</h4>
                        <ul class="list-disc list-inside text-gray-700 space-y-1 pl-4">
                            <li><strong>Tobacco Smoking:</strong> Cigarettes, cigars, pipes. Quantify pack-years. (Accounts for ~85% of cases)</li>
                            <li><strong>Secondhand Smoke Exposure:</strong> Significant risk.</li>
                            <li><strong>Occupational Exposures:</strong> Asbestos, radon, silica, diesel exhaust, arsenic, chromium, nickel.</li>
                            <li><strong>Diet and Physical Activity:</strong> Emerging evidence suggests protective effects of healthy lifestyles.</li>
                        </ul>
                    </div>
                    <div>
                        <h4 class="text-xl font-medium text-[#00B4D8] mb-2">🧬 Non-Modifiable Risk Factors:</h4>
                        <ul class="list-disc list-inside text-gray-700 space-y-1 pl-4">
                            <li><strong>Age:</strong> Risk increases significantly after age 50.</li>
                            <li><strong>Family History of Lung Cancer:</strong> Especially in first-degree relatives.</li>
                            <li><strong>Personal History of Lung Cancer:</strong> Increased risk of new primary or recurrence.</li>
                            <li><strong>Previous Lung Diseases:</strong> COPD, pulmonary fibrosis, tuberculosis.</li>
                            <li><strong>Genetic Predisposition:</strong> Rare inherited syndromes.</li>
                            <li><strong>Air Pollution:</strong> Outdoor and indoor (e.g., biomass fuel).</li>
                        </ul>
                    </div>
                    <p class="text-md text-gray-600 mt-6 text-center guideline-box p-4 rounded-lg">
                        <strong>Colombian Context:</strong> The Colombian Ministry of Health guidelines emphasize tobacco control as a primary prevention strategy and highlight the importance of assessing occupational exposures prevalent in certain regions or industries.
                    </p>
                </div>
            </div>
        </section>

        <section id="evaluation-screening" class="mb-12">
            <h2 class="text-3xl font-semibold mb-6 text-center section-title">The PCP's Role: Clinical Evaluation, Screening & Referral</h2>
            <p class="text-lg text-gray-700 mb-8 text-center max-w-3xl mx-auto">
                Primary care physicians are central to the early detection pathway. This involves astute clinical evaluation of symptomatic patients, appropriate use of screening tools for high-risk individuals, and timely referral to specialists. This section outlines key steps in evaluation and current screening recommendations based on NCCN, ASCO, and Colombian guidelines.
            </p>

            <div class="mb-8 bg-white p-6 rounded-lg shadow-xl">
                <h3 class="text-2xl font-semibold text-[#0077B6] mb-4">Simplified Diagnostic & Referral Pathway (Primary Care Focus)</h3>
                <p class="text-gray-700 mb-6">This flowchart outlines a general approach for primary care physicians when evaluating a patient with potential lung cancer symptoms or risk factors. It emphasizes timely investigation and referral according to current guidelines.</p>
                <div class="space-y-4">
                    <div class="flowchart-step p-4 rounded-lg text-center shadow">
                        <p class="font-semibold">1. Patient Presentation</p>
                        <p class="text-sm">Symptoms (e.g., persistent cough, dyspnea, hemoptysis) OR High-Risk Profile for Screening</p>
                    </div>
                    <div class="text-center flowchart-arrow text-3xl font-bold">↓</div>
                    <div class="flowchart-step p-4 rounded-lg text-center shadow">
                        <p class="font-semibold">2. Initial PCP Evaluation</p>
                        <p class="text-sm">Detailed History (symptoms, risk factors, smoking history, family history, occupational exposure), Physical Examination</p>
                    </div>
                    <div class="text-center flowchart-arrow text-3xl font-bold">↓</div>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 items-start">
                        <div class="flowchart-step p-4 rounded-lg text-center shadow">
                            <p class="font-semibold">3a. Low Suspicion / Non-Specific Symptoms</p>
                            <p class="text-sm">Consider Chest X-ray. If normal & symptoms persist, or if high-risk, re-evaluate or consider CT. Manage other potential causes.</p>
                        </div>
                        <div class="flowchart-step p-4 rounded-lg text-center shadow">
                             <p class="font-semibold">3b. High Suspicion / Red Flags / Abnormal CXR</p>
                            <p class="text-sm">Proceed to Diagnostic Chest CT (low-dose for screening, standard for symptoms).</p>
                        </div>
                    </div>
                     <div class="text-center flowchart-arrow text-3xl font-bold">↓</div>
                     <div class="flowchart-step p-4 rounded-lg text-center shadow">
                        <p class="font-semibold">4. CT Scan Findings</p>
                        <p class="text-sm">Normal: Continue routine care/risk factor management. Suspicious Nodule/Mass: Follow guideline-based nodule management (e.g., Lung-RADS for LDCT, Fleischner for incidental).</p>
                    </div>
                    <div class="text-center flowchart-arrow text-3xl font-bold">↓</div>
                    <div class="flowchart-step p-4 rounded-lg text-center shadow bg-[#ADE8F4]">
                        <p class="font-semibold">5. Referral to Specialist (Pulmonologist/Thoracic Oncologist)</p>
                        <p class="text-sm">For suspicious nodules requiring further workup (PET, biopsy), confirmed cancer, or complex cases. Ensure timely referral (e.g., within 2 weeks for high suspicion as per some guidelines).</p>
                    </div>
                </div>
                <p class="text-sm text-gray-600 mt-6 text-center">This is a simplified pathway. Always refer to specific, up-to-date clinical guidelines (NCCN, ASCO, Colombian MOH).</p>
            </div>

            <div class="bg-white p-6 rounded-lg shadow-xl">
                <h3 class="text-2xl font-semibold text-[#0077B6] mb-4 text-center">Lung Cancer Screening with Low-Dose CT (LDCT)</h3>
                <p class="text-gray-700 mb-6 text-center">LDCT screening is recommended for high-risk individuals and has been shown to reduce lung cancer mortality.</p>
                
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
                    <div class="guideline-box p-4 rounded-lg">
                        <h4 class="text-xl font-medium text-[#0077B6] mb-2">NCCN/ASCO General Eligibility Criteria (Example):</h4>
                        <ul class="list-disc list-inside text-gray-700 space-y-1">
                            <li>Age 50-80 years (ASCO/NCCN vary slightly, check specific guideline)</li>
                            <li>≥20 pack-year smoking history</li>
                            <li>Current smoker or quit within the past 15 years</li>
                            <li>Sufficiently healthy to undergo potential treatment</li>
                            <li>Shared decision-making discussion completed</li>
                        </ul>
                    </div>
                     <div class="guideline-box p-4 rounded-lg">
                        <h4 class="text-xl font-medium text-[#0077B6] mb-2">Key Benefits & Considerations:</h4>
                        <ul class="list-disc list-inside text-gray-700 space-y-1">
                            <li>Reduces lung cancer mortality by ~20-26% in screened populations.</li>
                            <li>Potential harms: False positives, overdiagnosis, radiation exposure, anxiety.</li>
                            <li>Requires adherence to annual screening and structured reporting (e.g., Lung-RADS).</li>
                            <li>Crucial: Smoking cessation counseling should accompany screening.</li>
                        </ul>
                    </div>
                </div>
                <p class="text-md text-gray-600 mt-4 text-center">
                    <strong>Colombian Guidelines:</strong> The Colombian Ministry of Health guideline acknowledges the evidence for LDCT screening and provides recommendations for its implementation within the Colombian healthcare system, often emphasizing a risk-adapted approach and shared decision-making.
                </p>
                <div class="chart-container mx-auto h-[300px] md:h-[350px] mt-6">
                    <canvas id="screeningImpactChart"></canvas>
                </div>
                <p class="text-sm text-gray-600 mt-4 text-center">Illustrative data showing potential mortality reduction with LDCT screening programs.</p>
            </div>
        </section>

        <section id="case-studies" class="mb-12">
            <h2 class="text-3xl font-semibold mb-6 text-center section-title">Learning in Practice: Key Insights from Clinical Scenarios</h2>
            <p class="text-lg text-gray-700 mb-8 text-center max-w-3xl mx-auto">
                Applying guideline-based knowledge to real-world patient encounters is key. While detailed case studies are extensive, this section distills critical learning points relevant to primary care physicians, reflecting common challenges and best practices in early lung cancer identification, inspired by typical scenarios discussed in training and guidelines (e.g., SEOM-GECP for SCLC, NCCN for NSCLC).
            </p>

            <div id="tabs-container" class="bg-white p-6 rounded-lg shadow-xl">
                <div class="flex border-b border-gray-300">
                    <button class="tab active" onclick="openTab(event, 'case1')">Scenario 1: The Persistent Cough</button>
                    <button class="tab" onclick="openTab(event, 'case2')">Scenario 2: The High-Risk Smoker</button>
                </div>

                <div id="case1" class="tab-content active">
                    <h4 class="text-xl font-semibold text-[#0077B6] mb-3">Scenario 1: The Persistent Cough in a 62-Year-Old Smoker</h4>
                    <p class="text-gray-700 mb-2"><strong>Presentation:</strong> A 62-year-old male with a 40 pack-year smoking history presents with a cough lasting 8 weeks, initially dry, now occasionally productive of clear sputum. Denies fever or hemoptysis. Reports mild fatigue. Initial chest X-ray reported as "age-related changes, no acute process."</p>
                    <p class="text-gray-700 mb-2"><strong>PCP Action & Rationale (Guideline-Based):</strong></p>
                    <ul class="list-disc list-inside space-y-1 text-gray-700 pl-4 mb-3">
                        <li><strong>High Index of Suspicion:</strong> Despite "normal" CXR, persistent cough in a heavy smoker is a warning. CXR has limited sensitivity for early lung cancers. (NCCN, Colombian MOH)</li>
                        <li><strong>Further Investigation:</strong> Ordered a diagnostic chest CT scan.</li>
                        <li><strong>CT Finding:</strong> Revealed a 1.5 cm solid nodule in the right upper lobe.</li>
                        <li><strong>Referral:</strong> Prompt referral to a pulmonologist.</li>
                    </ul>
                    <p class="text-gray-700 mb-2"><strong>Outcome & Learning Points:</strong></p>
                     <ul class="list-disc list-inside space-y-1 text-gray-700 pl-4">
                        <li>Biopsy confirmed Stage IA adenocarcinoma. Patient underwent successful surgical resection.</li>
                        <li><strong>Key Takeaway for PCPs:</strong> Do not dismiss persistent respiratory symptoms in high-risk patients even with a normal/non-specific CXR. Maintain a low threshold for ordering a chest CT. Early referral is critical.</li>
                    </ul>
                </div>

                <div id="case2" class="tab-content">
                    <h4 class="text-xl font-semibold text-[#0077B6] mb-3">Scenario 2: Asymptomatic High-Risk Individual for Screening</h4>
                    <p class="text-gray-700 mb-2"><strong>Presentation:</strong> A 58-year-old female, current smoker with a 30 pack-year history, presents for an annual check-up. She is asymptomatic. Expresses interest in "cancer screening."</p>
                    <p class="text-gray-700 mb-2"><strong>PCP Action & Rationale (Guideline-Based):</strong></p>
                    <ul class="list-disc list-inside space-y-1 text-gray-700 pl-4 mb-3">
                        <li><strong>Screening Eligibility Assessment:</strong> Patient meets NCCN/ASCO criteria for LDCT screening (age, smoking history).</li>
                        <li><strong>Shared Decision-Making:</strong> Discussed benefits (mortality reduction) and potential harms (false positives, overdiagnosis, radiation) of LDCT screening. Provided smoking cessation counseling and resources. (ASCO, Colombian MOH)</li>
                        <li><strong>Screening Order:</strong> Patient opted for screening; LDCT ordered.</li>
                        <li><strong>LDCT Finding:</strong> Lung-RADS 2 (benign appearance nodule), recommend continued annual screening.</li>
                    </ul>
                    <p class="text-gray-700 mb-2"><strong>Outcome & Learning Points:</strong></p>
                     <ul class="list-disc list-inside space-y-1 text-gray-700 pl-4">
                        <li>Patient continues annual LDCT screening and smoking cessation efforts.</li>
                        <li><strong>Key Takeaway for PCPs:</strong> Proactively identify and engage eligible high-risk patients in shared decision-making about LDCT screening. Integrate smoking cessation as a core component of any screening discussion. Understand Lung-RADS categories for appropriate follow-up.</li>
                    </ul>
                </div>
            </div>
             <p class="text-md text-gray-600 mt-8 text-center guideline-box p-4 rounded-lg">
                <strong>Practice Point (SEOM-GECP for SCLC):</strong> While many early detections are NSCLC, rapid progression is characteristic of SCLC. Any suspicion of SCLC (e.g., rapid onset symptoms, paraneoplastic syndromes, bulky central masses) warrants extremely urgent referral and diagnostic workup, as treatment strategies differ significantly.
            </p>
        </section>
        
        <section id="conclusion" class="mb-12 py-10 bg-[#0077B6] text-white rounded-lg shadow-xl px-6">
            <h2 class="text-3xl font-semibold mb-6 text-center">Empowering Primary Care: A Call to Action for Early Lung Cancer Detection</h2>
            <p class="text-lg mb-8 text-center max-w-3xl mx-auto">
                The fight against lung cancer hinges significantly on early detection, and primary care physicians are indispensable in this effort. By maintaining a high index of suspicion, diligently assessing risk factors, recognizing subtle signs, appropriately utilizing screening tools, and ensuring timely referrals, PCPs can profoundly impact patient outcomes.
            </p>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-6 text-center">
                <div class="bg-[#00B4D8] p-6 rounded-lg shadow-md">
                    <h3 class="text-xl font-semibold mb-2">EDUCATE & ENGAGE</h3>
                    <p>Continuously update knowledge on guidelines. Engage patients in discussions about risk and prevention.</p>
                </div>
                <div class="bg-[#00B4D8] p-6 rounded-lg shadow-md">
                    <h3 class="text-xl font-semibold mb-2">IDENTIFY & SCREEN</h3>
                    <p>Proactively identify high-risk individuals for LDCT screening. Implement shared decision-making.</p>
                </div>
                <div class="bg-[#00B4D8] p-6 rounded-lg shadow-md">
                    <h3 class="text-xl font-semibold mb-2">REFER PROMPTLY</h3>
                    <p>Ensure swift referral to specialists for suspicious findings to expedite diagnosis and treatment.</p>
                </div>
            </div>
            <p class="text-center mt-8 text-lg">
                Together, through vigilance and adherence to evidence-based practices, we can shift the paradigm towards earlier diagnosis and give our patients the best chance for a cure.
            </p>
        </section>

    </main>

    <footer class="bg-gray-800 text-white py-8 px-4 text-center">
        <p class="mb-2">&copy; 2025 Lung Cancer Early Detection Initiative. For educational purposes only.</p>
        <p class="text-sm">Based on information from Colombian Ministry of Health, NCCN, ASCO, SEOM-GECP guidelines (2024-2025 where available).</p>
        <p class="text-xs mt-2">This infographic is a conceptual representation and does not replace clinical guidelines or professional medical advice.</p>
    </footer>

    <script>
        function wrapLabels(label, maxWidth) {
            if (typeof label !== 'string') {
                return label; // Return as is if not a string (e.g., already an array)
            }
            if (label.length <= maxWidth) {
                return label;
            }
            const words = label.split(' ');
            let currentLine = '';
            const lines = [];
            for (const word of words) {
                if ((currentLine + word).length > maxWidth && currentLine.length > 0) {
                    lines.push(currentLine.trim());
                    currentLine = '';
                }
                currentLine += word + ' ';
            }
            lines.push(currentLine.trim());
            return lines;
        }

        const tooltipTitleCallback = function(tooltipItems) {
            const item = tooltipItems[0];
            let label = item.chart.data.labels[item.dataIndex];
            if (Array.isArray(label)) {
              return label.join(' ');
            } else {
              return label;
            }
        };

        const commonChartOptions = {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    labels: {
                        color: '#333333', // Dark gray for legend text
                        font: { size: 12 }
                    }
                },
                tooltip: {
                    callbacks: {
                        title: tooltipTitleCallback
                    },
                    backgroundColor: 'rgba(0, 0, 0, 0.8)',
                    titleFont: { size: 14 },
                    bodyFont: { size: 12 },
                    padding: 10
                }
            },
            scales: {
                y: {
                    beginAtZero: true,
                    ticks: { 
                        color: '#4A5568', // Tailwind gray-700
                        font: { size: 12 }
                    },
                    grid: { color: '#E2E8F0' } // Tailwind gray-300
                },
                x: {
                    ticks: { 
                        color: '#4A5568',
                        font: { size: 12 },
                        callback: function(value, index, ticks) {
                            const label = this.getLabelForValue(value);
                            return wrapLabels(label, 16); // Wrap x-axis labels
                        }
                    },
                    grid: { display: false }
                }
            }
        };
        
        const pieDonutOptions = {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'top',
                    labels: { 
                        color: '#333333',
                        font: { size: 12 },
                         boxWidth: 20,
                         padding: 15,
                         generateLabels: function(chart) {
                            const data = chart.data;
                            if (data.labels.length && data.datasets.length) {
                                return data.labels.map(function(label, i) {
                                    const meta = chart.getDatasetMeta(0);
                                    const style = meta.controller.getStyle(i);
                                    let fullLabel = label;
                                    if (Array.isArray(label)) {
                                        fullLabel = label.join(' ');
                                    }
                                    return {
                                        text: wrapLabels(fullLabel, 20), // Wrap legend labels
                                        fillStyle: style.backgroundColor,
                                        strokeStyle: style.borderColor,
                                        lineWidth: style.borderWidth,
                                        hidden: isNaN(data.datasets[0].data[i]) || meta.data[i].hidden,
                                        index: i
                                    };
                                });
                            }
                            return [];
                        }
                    }
                },
                tooltip: {
                    callbacks: {
                        title: tooltipTitleCallback,
                        label: function(context) {
                            let label = context.dataset.label || '';
                            if (label) {
                                label += ': ';
                            }
                            if (context.parsed !== null) {
                                label += context.parsed + '%';
                            }
                            return label;
                        }
                    },
                    backgroundColor: 'rgba(0, 0, 0, 0.8)',
                    titleFont: { size: 14 },
                    bodyFont: { size: 12 },
                    padding: 10
                }
            }
        };


        // Chart 1: Stage at Diagnosis
        const stageAtDiagnosisCtx = document.getElementById('stageAtDiagnosisChart').getContext('2d');
        new Chart(stageAtDiagnosisCtx, {
            type: 'doughnut',
            data: {
                labels: [wrapLabels('Stage I (Localized)',16), wrapLabels('Stage II (Localized)',16), wrapLabels('Stage III (Regional)',16), wrapLabels('Stage IV (Distant)',16)],
                datasets: [{
                    label: 'Stage at Diagnosis',
                    data: [20, 15, 25, 40], // Example percentages
                    backgroundColor: ['#00B4D8', '#90E0EF', '#ADE8F4', '#0077B6'],
                    borderColor: '#FFFFFF',
                    borderWidth: 2
                }]
            },
            options: pieDonutOptions
        });

        // Chart 2: Global Lung Cancer Stats
        const globalLungCancerStatsCtx = document.getElementById('globalLungCancerStatsChart').getContext('2d');
        new Chart(globalLungCancerStatsCtx, {
            type: 'bar',
            data: {
                labels: [wrapLabels('Estimated New Cases',16), wrapLabels('Estimated Deaths',16)],
                datasets: [{
                    label: 'Global Annual Figures',
                    data: [2300000, 1800000], // Example data
                    backgroundColor: ['#0077B6', '#00B4D8'],
                    borderColor: ['#005A8D', '#008FB0'],
                    borderWidth: 1
                }]
            },
            options: commonChartOptions
        });

        // Chart 3: Colombian Lung Cancer Stats
        const colombianLungCancerStatsCtx = document.getElementById('colombianLungCancerStatsChart').getContext('2d');
        new Chart(colombianLungCancerStatsCtx, {
            type: 'bar',
            data: {
                labels: [wrapLabels('Estimated New Cases (Colombia)',25), wrapLabels('Estimated Deaths (Colombia)',25)],
                datasets: [{
                    label: 'Colombian Annual Figures',
                    data: [12000, 10500], // Example data
                    backgroundColor: ['#ADE8F4', '#90E0EF'],
                    borderColor: ['#00A2C7', '#00B4D8'],
                    borderWidth: 1
                }]
            },
            options: commonChartOptions
        });
        
        // Chart 4: Lung Cancer Proportion of All Cancer Deaths
        const lungCancerProportionOfDeathsCtx = document.getElementById('lungCancerProportionOfDeathsChart').getContext('2d');
        new Chart(lungCancerProportionOfDeathsCtx, {
            type: 'pie',
            data: {
                labels: [wrapLabels('Lung Cancer Deaths',16), wrapLabels('Other Cancer Deaths',16)],
                datasets: [{
                    label: 'Proportion of Cancer Deaths',
                    data: [18, 82], // Example: 18% Lung Cancer
                    backgroundColor: ['#0077B6', '#CAF0F8'],
                    borderColor: '#FFFFFF',
                    borderWidth: 2
                }]
            },
            options: pieDonutOptions
        });

        // Chart 5: Risk Factor Contribution
        const riskFactorContributionCtx = document.getElementById('riskFactorContributionChart').getContext('2d');
        new Chart(riskFactorContributionCtx, {
            type: 'bar',
            data: {
                labels: [
                    wrapLabels('Tobacco Smoking',16), 
                    wrapLabels('Radon Exposure',16), 
                    wrapLabels('Occupational Exposures',20), 
                    wrapLabels('Air Pollution',16),
                    wrapLabels('Family History',16)
                ],
                datasets: [{
                    label: 'Attributable Risk Percentage (Illustrative)',
                    data: [85, 10, 8, 5, 3], // Example percentages, not additive for all cases
                    backgroundColor: ['#0077B6', '#00B4D8', '#90E0EF', '#ADE8F4', '#CAF0F8'],
                    borderColor: '#005A8D',
                    borderWidth: 1
                }]
            },
            options: { ...commonChartOptions, indexAxis: 'y' } // Horizontal bar chart
        });
        
        // Chart 6: Screening Impact Chart
        const screeningImpactCtx = document.getElementById('screeningImpactChart').getContext('2d');
        new Chart(screeningImpactCtx, {
            type: 'bar',
            data: {
                labels: [wrapLabels('Mortality without Screening',25), wrapLabels('Mortality with LDCT Screening',25)],
                datasets: [{
                    label: 'Relative Lung Cancer Mortality',
                    data: [100, 75], // Example: 25% reduction
                    backgroundColor: ['#00B4D8', '#0077B6'],
                    borderColor: ['#008FB0', '#005A8D'],
                    borderWidth: 1
                }]
            },
             options: {
                ...commonChartOptions,
                scales: {
                    ...commonChartOptions.scales,
                    y: {
                        ...commonChartOptions.scales.y,
                        title: {
                            display: true,
                            text: 'Relative Mortality Rate (%)',
                            color: '#005A8D',
                            font: { size: 14, weight: 'bold' }
                        }
                    }
                }
            }
        });

        // Tab functionality
        function openTab(event, tabName) {
            let i, tabcontent, tablinks;
            tabcontent = document.getElementsByClassName("tab-content");
            for (i = 0; i < tabcontent.length; i++) {
                tabcontent[i].style.display = "none";
            }
            tablinks = document.getElementsByClassName("tab");
            for (i = 0; i < tablinks.length; i++) {
                tablinks[i].className = tablinks[i].className.replace(" active", "");
            }
            document.getElementById(tabName).style.display = "block";
            event.currentTarget.className += " active";
        }
        // Initialize first tab
        if (document.getElementsByClassName("tab active").length > 0) {
