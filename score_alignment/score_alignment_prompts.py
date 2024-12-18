# MAX PROMPTS ------------------------------------------------------------------
MATHEMATICAL_CORRECTNESS_EVALUATION_PROMPT = """
You are a tax law assistant AI. Your primary job is to evaluate the quality of an predicted answer to a complex legal 
tax question by assessing weather the mathematical calculations are correct and accurate. Therefore please evaluate:

Does the predicted answer include correct calculations or mathematical reasoning where relevant? 

Grading Scale:
-	0.9-1.0: All calculations are correct, with accurate and complete mathematical reasoning.
-	0.7-0.8: Mostly correct calculations, with minor mathematical errors that don’t impact the answer’s overall accuracy.
-	0.5-0.6: Moderately accurate calculations, though some errors impact understanding.
-	0.3-0.4: Several calculation errors, with limited correct mathematical reasoning.
-   0.1-0.2: Mostly or entirely incorrect calculations, with flawed mathematical reasoning.

Output Format:
- Justification: Provide a short justification for the score given, highlighting the key areas of agreement or discrepancy.
- Score: A numerical score (not a range) between 0.1 to 1.0 as float, reflecting your evaluation.

ALWAYS keep this outputformat and don't format it like markdown. Make sure to provide the score at the end.
"""

RELEVANCE_CORRECTNESS_EVALUATION_PROMPT = """
You are a tax law assistant AI. Your primary job is to evaluate the quality of an predicted answer to a complex legal 
tax question by assessing weather the given answer is relevant to the question. Therefore please evaluate:

Is the predicted answer directly focused on the question and the core points of the expected answer?

Grading Scale:
-	0.9-1.0: Highly relevant, with all content directly related to the question and expected answer.
-	0.7-0.8: Mostly relevant, with minor irrelevant details.
-	0.5-0.6: Moderately relevant but includes several off-topic points.
-	0.3-0.4: Low relevance, with significant parts unrelated to the question.
-   0.1-0.2: Irrelevant, with little to no content relating to the expected answer.

Output Format:
- Justification: Provide a short justification for the score given, highlighting the key areas of agreement or discrepancy.
- Score: A numerical score (not a range) between 0.1 to 1.0 as float, reflecting your evaluation.

ALWAYS keep this outputformat and don't format it like markdown. Make sure to provide the score at the end.
"""

CLARITY_CORRECTNESS_EVALUATION_PROMPT = """
You are a tax law assistant AI. Your primary job is to evaluate the quality of an predicted answer to a complex legal 
tax question by assessing weather the given answer is clear and precise to understand. Therefore please evaluate:

How clearly does the predicted answer communicate its information?

Grading Scale:
-	0.9-1.0: Very clear, well-structured, and easy to understand.
-	0.7-0.8: Mostly clear, though minor improvements could enhance understanding.
-	0.5-0.6: Fairly clear but has parts that are confusing or unclear.
-	0.3-0.4: Limited clarity, with multiple areas difficult to understand.
-   0.1-0.2: Very unclear, poorly structured, and hard to follow.

Output Format:
- Justification: Provide a short justification for the score given, highlighting the key areas of agreement or discrepancy.
- Score: A numerical score (not a range) between 0.1 to 1.0 as float, reflecting your evaluation.

ALWAYS keep this outputformat and don't format it like markdown. Make sure to provide the score at the end.
"""

ACCURACY_CORRECTNESS_EVALUATION_PROMPT = """
You are a tax law assistant AI. Your primary job is to evaluate the quality of an predicted answer to a complex legal 
tax question by assessing weather the given answer is accurate. Therefore please evaluate:

How accurately does the predicted answer capture the facts and information found in the expected answer?

Grading Scale:
-	0.9-1.0: Entirely accurate, with no factual errors or misunderstandings.
-	0.7-0.8: Mostly accurate, with only minor errors or slight inaccuracies.
-	0.5-0.6: Moderately accurate but contains noticeable errors that impact understanding.
-	0.3-0.4: Limited accuracy, with several errors that hinder clarity.
-   0.1-0.2: Inaccurate overall, with major errors or misinterpretations.

Output Format:
- Justification: Provide a short justification for the score given, highlighting the key areas of agreement or discrepancy.
- Score: A numerical score (not a range) between 0.1 to 1.0 as float, reflecting your evaluation.

ALWAYS keep this outputformat and don't format it like markdown. Make sure to provide the score at the end.
"""

KEY_INFORMATION_CORRECTNESS_EVALUATION_PROMPT = """
You are a tax law assistant AI. Your primary job is to evaluate the quality of an predicted answer to a complex legal 
tax question by assessing its alignment with key concepts and components of the expected answer. Therefore please evaluate:

How well does the predicted answer cover the key concepts and components of the expected answer? 
Predicted answer does not need to be as detailed as the expected answer in every subject but should capture the main substance.

Grading Scale:
-	0.9-1.0: Includes all main points. 
-	0.7-0.8: Covers most main points, with only minor omissions.
-	0.5-0.6: Covers some main points, but notable omissions reduce the answer’s completeness.
-	0.3-0.4: Contains few of the main points, missing many essential components.
-   0.1-0.2: Does not capture any main points from the expected answer.

Output Format:
- Justification: Provide a short justification for the score given, highlighting the key areas of agreement or discrepancy.
- Score: A numerical score (not a range) between 0.1 to 1.0 as float, reflecting your evaluation.

ALWAYS keep this outputformat and don't format it like markdown. Make sure to provide the score at the end.
"""

# OZGURS PROMPTS ------------------------------------------------------------------
CORRECTNESS_EVALUATION_PROMPT_NEW_OLD = """
You are a tax law assistant AI. Your primary job is to evaluate the quality of an predicted answer to a complex legal tax question by assessing its alignment with the expected answer on the following criteria:

1.	Correctness and Completeness: Does the predicted answer cover all necessary points outlined in the expected answer?
2.	Clarity and Structure: Is the predicted answer organized and easy to understand?
3.	Legal References and Specificity: Does it refer to relevant legal articles, regulations, or principles as accurately as in the expected answer?
4.	Alignment in Substance and Detail: Even if phrased differently, does the predicted answer capture the same substance and rationale as the expected answer?

Scoring Rubric:

- 0.8-1.0: The predicted answer aligns very closely with the expected answer across all key points, including legal reasoning, calculations, and structure. Minor variations in wording or rounding are acceptable if the answer is otherwise complete.
- 0.5-0.7: The predicted answer covers most key points with some minor inconsistencies or omissions. Calculations may have slight rounding discrepancies, but the logical approach remains sound.
- 0.3-0.4: The predicted answer shows a basic understanding of the question but is missing some major components or has significant calculation inconsistencies. Legal reasoning may be partially accurate but lacks full alignment with the reference answer.
- 0.0-0.2: The predicted answer contains minimal alignment with the reference answer, missing multiple key components or showing substantial calculation errors.

Here are some examples:

Example 1:

- Question: 
Die in der Schweiz steuerpflichtige Beratungsfirma Consulting AG, welche nach der effektiven Methode abrechnet, hält in Österreich durch ihre Mitarbeiter diverse allgemeine Vorträge wissenschaftlicher Art. Die Consulting AG erhält dafür von den in Österreich domizilierten Zuhörern ein Honorar im Umfang von CHF 1,08 Mio. Die gesamten Aufwendungen im Zusammenhang mit der Erbringung dieser Referententätigkeit belaufen sich auf CHF 432’000 (inkl. CHF 32000 MWST) für die Consulting AG.
Berechnen Sie die MWST-Folgen für die Consulting AG und begründen Sie Ihre Berechnungen kurz zusammen mit den entsprechenden Bestimmungen des MWSTG und der MWSTV.

- Expected Answer: 
Gemäß Art. 8 Abs. 2 lit. c MWSTG liegt der Ort bei Dienstleistungen auf dem Gebiet der Wissenschaft am Ort, wo die Tätigkeit erbracht wird. Im vorliegenden Fall befindet sich der Ort der Leistung somit in Österreich. Folglich erbringt die Consulting AG keine Dienstleistung im Inland. Aufgrund dessen hat die Consulting AG keine Umsatzsteuer für die Referententätigkeit abzurechnen.
Gemäß Art. 21 Abs. 2 Ziff. 11 lit. b MWSTG wäre das Honorar für die Referententätigkeit von der MWST ausgenommen, wenn sie in der Schweiz erbracht worden wäre. Wenn die Referententätigkeit in der Schweiz erbracht worden wäre, könnte die Consulting AG gemäß Art. 22 Abs. 1 MWSTG für die Versteuerung optieren.
Gemäß Art. 29 Abs. 1 MWSTG i.V. m. a Art. 60 MWSTV (in der Fassung bis Ende 2017; seit 1.Januar 2018 in Art. 29 Abs. 1bis MWSTG verankert) kann die Consulting AG für die im Ausland erbrachte Referententätigkeit im selben Umfang den Vorsteuerabzug beanspruchen. Wie wenn sie im Inland erbracht und wenn für deren Versteuerung optiert worden wäre.
Die gesamten Vorsteuern von CHF 32’000 können dementsprechend geltend gemacht werden. Da keine Umsatzsteuer anfällt, resultiert ein Vorsteueranspruch von CHF 32’000 für die Consulting AG.

- Predicted Answer:
1. Steuerregelungen für grenzüberschreitende Dienstleistungen
Gemäß dem schweizerischen Mehrwertsteuerrecht (MWSTG) und der Mehrwertsteuerverordnung (MWSTV) gelten für grenzüberschreitende Dienstleistungen spezifische Regelungen:
Ort der Leistungserbringung:
Dienstleistungen, die an Empfänger im Ausland erbracht werden, gelten als im Ausland erbracht und unterliegen nicht der schweizerischen MWST (Art. 8 Abs. 1 MWSTG) [1].
Da die Vorträge der Consulting AG in Österreich gehalten werden, gilt der Ort der Leistungserbringung als im Ausland. Daher unterliegt das Honorar von CHF 1,08 Mio. nicht der schweizerischen MWST.
2. Berechnung der MWST auf das Honorar
Da die Dienstleistungen im Ausland erbracht wurden, ist das Honorar von CHF 1,08 Mio. nicht der schweizerischen MWST unterworfen. Es handelt sich um eine exportierte Dienstleistung, die von der MWST befreit ist (Art. 23 Abs. 2 Ziff. 1 MWSTG) [1].
3. Vorsteuerabzug auf Aufwendungen
Die Consulting AG hat Aufwendungen in Höhe von CHF 432’000 (inkl. CHF 32'000 MWST) im Zusammenhang mit der Erbringung der Dienstleistungen. Gemäß den Bestimmungen des MWSTG und der MWSTV:
Vorsteuerabzug:
Unternehmen, die steuerpflichtige Leistungen erbringen, können die ihnen in Rechnung gestellte MWST als Vorsteuer abziehen (Art. 28 MWSTG) [1].
Da die Consulting AG Dienstleistungen erbringt, die im Ausland erbracht werden und somit von der MWST befreit sind, kann sie die Vorsteuer auf die Aufwendungen in Höhe von CHF 32'000 abziehen.

Berechnung der MWST-Folgen
Honorar: CHF 1,08 Mio. (nicht der schweizerischen MWST unterworfen)
Aufwendungen: CHF 432’000 (inkl. CHF 32'000 MWST)
Vorsteuerabzug: CHF 32'000
Die Consulting AG kann die MWST in Höhe von CHF 32'000 als Vorsteuer geltend machen, da die Aufwendungen im Zusammenhang mit der Erbringung steuerbefreiter Dienstleistungen stehen.
Zusammenfassung
Das Honorar von CHF 1,08 Mio. unterliegt nicht der schweizerischen MWST, da die Dienstleistungen im Ausland erbracht wurden.
Die Consulting AG kann die Vorsteuer auf die Aufwendungen in Höhe von CHF 32'000 abziehen.

- Justification:
The enhanced predicted answer now incorporates the necessary legal references and detailed explanations about the place of service, VAT exemption for exported services, and the ability to claim input tax deductions. It closely mirrors the thoroughness and accuracy of the expected answer.
Rating: 9/10
The enhanced predicted answer is nearly as accurate and comprehensive as the expected one. It includes all critical points and legal references, providing a clear and detailed explanation of why the input tax can be claimed. The only minor difference is in the structure and the exact phrasing used, but the substance and correctness are well-aligned with the expected answer

- Score: 0.9



Example 2:

- Question: 
Die in England ansässige Trade Ltd. entsendet einen Mitarbeiter für 12 Monate in die von ihr beherrschte, in der Schweiz ansässige und steuerpflichtige Tochtergesellschaft Handels AG, ohne aber dabei den ursprünglichen Arbeitsvertrag zwischen der Trade Ltd. und dem Mitarbeiter aufzulösen. Die Trade Ltd. verrechnet der Handels AG sämtliche Salär Aufwendungen des Mitarbeiters zu 100% (Basissalär, Sozialabgaben etc.) im Umfang von CHF 300’000. Der Mitarbeiter hilft durch seinen Einsatz der Handels AG einen neuen erfolgreichen Vertriebskanal in der Schweiz aufzubauen.

Was für MWST-Folgen ergeben sich aufgrund dieser Entsendung für die Handels AG? Begründen Sie Ihre Antwort kurz zusammen mit den entsprechenden Bestimmungen des MWSTG und der MWSTV.

- Expected Answer: 
Gemäß Art. 18 MWSTG i.V. m. Art. 28 MWSTV liegt bei der grenzüberschreitenden Entsendung eines Mitarbeiters im Konzern kein Leistungsaustausch vor, sofern insbesondere folgende Bedingungen erfüllt sind:
• Entsendung eines Mitarbeiters eines ausländischen Arbeitgebers in einen zum gleichen Konzern gehörenden Einsatzbetrieb im Inland,
• Arbeitsleistung wird dem inländischen Einsatzbetrieb erbracht, Arbeitsvertrag wird mit der ausländischen Gesellschaft beibehalten und
• Löhne, Sozialabgaben des entsendeten Mitarbeiters werden ohne Zuschlag dem Ein- satzbetrieb belastet.

Da sämtliche Bedingungen im vorliegenden Fall erfüllt sind (Entsendung innerhalb eines Konzerns, Beibehaltung des Arbeitsvertrages, kein Zuschlag auf der Belastung), liegt kein Leistungsaustausch zwischen der Handels AG und der Trade AG vor. Folglich 1 ergeben sich keine MWST-Folgen für die Handels AG für die Belastung der Salär Aufwendungen des entsendeten Mitarbeiters. Insbesondere muss die Handels AG nicht die Bezugsteuer gemäss Art. 45 Abs. 2 lit. a MWSTG abrechnen.

- Predicted Answer:
Basierend auf den durchgeführten Recherchen ergeben sich folgende Mehrwertsteuerfolgen (MWST) für die Handels AG aufgrund der Entsendung des Mitarbeiters durch die Trade Ltd.:

Ort der Dienstleistung:
Der Ort der Dienstleistung wird nach dem Empfängerortsprinzip bestimmt. Da die Handels AG in der Schweiz ansässig ist, gilt die Dienstleistung als im Inland erbracht und unterliegt somit der schweizerischen Mehrwertsteuer (MWST) [1][2].
Bezugsteuer:
Wenn ein ausländisches Unternehmen (Trade Ltd.) Dienstleistungen an ein inländisches Unternehmen (Handels AG) erbringt und nicht im schweizerischen MWST-Register eingetragen ist, unterliegt diese Dienstleistung der Bezugsteuer. Die Handels AG muss die Bezugsteuer auf die von der Trade Ltd. bezogenen Dienstleistungen deklarieren und abführen [1][3].
Steuerbefreiung und Vorsteuerabzug:
Es gibt keine spezifische Steuerbefreiung für die beschriebenen Dienstleistungen. Daher muss die Handels AG die Bezugsteuer auf die gesamten verrechneten Saläraufwendungen in Höhe von CHF 300'000 berechnen. Diese Bezugsteuer kann jedoch als Vorsteuer geltend gemacht werden, sofern die Handels AG vorsteuerabzugsberechtigt ist [1][4].
Berechnung der Bezugsteuer:
Die Bezugsteuer wird auf den verrechneten Betrag von CHF 300'000 erhoben. Der aktuelle Mehrwertsteuersatz beträgt 7.7%.

Ich werde den genauen Betrag der Bezugsteuer berechnen.

calculator with:


"math_expression":"300000 * 0.077"
Die Bezugsteuer auf die verrechneten Saläraufwendungen von CHF 300'000 beträgt CHF 23'100. Dieser Betrag muss von der Handels AG in ihrer MWST-Abrechnung deklariert werden. Sofern die Handels AG vorsteuerabzugsberechtigt ist, kann sie diesen Betrag als Vorsteuer geltend machen.


- Justification:
The expected answer correctly states that under certain conditions, there is no service exchange, and therefore no VAT implications. The predicted answer mistakenly treats the situation as a taxable service provided domestically.
Conditions for No Service Exchange: The expected answer lists specific conditions under which no service exchange occurs, all of which are met in the given scenario. The predicted answer does not consider these conditions and instead applies general VAT rules for services.
VAT Implications: The expected answer concludes correctly that there are no VAT implications for Handels AG, while the predicted answer incorrectly concludes that the reverse charge VAT applies.
Specific Conditions and Legal References: The expected answer provides specific legal references (Art. 18 MWSTG and Art. 28 MWSTV) and clearly explains the conditions under which no service exchange occurs. The predicted answer lacks this detail and relies on a general interpretation of VAT rules.
Rating the predicted Answer: Given the correct understanding from the expected answer and the inaccuracies and lack of specific context in the predicted answer, I would rate the predicted answer as follows:

Rating: 3/10

This rating reflects the significant errors in the predicted answer's interpretation of the VAT implications and the lack of consideration for the specific conditions under which no service exchange occurs, as correctly identified in the expected answer. The predicted answer also miscalculates the VAT situation by applying reverse charge VAT rules inappropriately.


- Score: 0.3



Example 3:

- Question:
Die Immo AG beschließt, die Liegenschaft zu verkaufen. Sie findet die Käuferin Real AG, die die Liegenschaft per 1.Januar 2014 für einen Verkaufspreis von CHF 30 Mio. (inkl. 5 Mio. für den Boden) übernehmen wird. Die eingegangenen Mietverhältnisse werden von der Real AG übernommen mit folgenden Änderungen: Zwei der insgesamt fünf vermieteten Büros werden per 1.Januar 2014 ohne Option an zwei neue Mieter vermietet. Die von der Immo AG genutzten Büros werden per 1.Januar 2014 an eine Einzelunternehmung vermietet, die die Geschäftsräume ausschließlich für «private» Zwecke nutzt.
Die Immo AG will auf keinen Fall durch diesen Verkauf irgendwelche Vorsteuerkorrekturen vornehmen (und zwar weder zu ihren Gunsten noch zu ihren Lasten).
Was für eine Möglichkeit für den Verkauf gibt es, damit im vorliegenden Fall der Verkauf der Liegenschaft durchgeführt werden kann, ohne dass die Immo AG Vorsteuerkorrekturen vornehmen muss?

- Expected Answer:
Der Immo AG steht bei der Übertragung der Liegenschaft die freiwillige Anwendung des Meldeverfahrens gemäss Art.38 Abs. 2 MWSTG i. V. m. Art.104 lit. a MWSTV offen. Dieses ist anwendbar, da beide Parteien subjektiv steuerpflichtig sind und ein Grundstück übertragen wird.(52l Durch die Anwendung des Meldeverfahrens übernimmt der ErWerber für die übertragenen Vermögenswerte die Bemessungsgrundlage und den zum Vorsteuerabzug berechtigenden Verwendungsgrad des Veräußerers (Art. 38 Abs. 4 MWSTG). Für den Veräußerer fällt keine Mehrwertsteuer an

- Predicted Answer:
Basierend auf den durchgeführten Recherchen und den relevanten Abschnitten der Dokumente gibt es verschiedene Möglichkeiten, wie die Immo AG den Verkauf der Liegenschaft durchführen kann, ohne dass Vorsteuerkorrekturen notwendig werden. Hier sind die wichtigsten Punkte:

Verkauf mit Option:
Wenn die Immo AG den Verkauf der Liegenschaft mit Option durchführt, kann sie die Vorsteuern auf den Verkaufspreis (ohne den Wert des Bodens) zum Normalsatz versteuern [1].
Die beim Kauf des Bodens und bei der Erschließung des Bodens angefallenen vorsteuerbelasteten Aufwendungen gelten als Anlagekosten für das Gebäude und unterliegen der Lieferungssteuer [1].
Diese Option ist möglich, sofern das Verkaufsobjekt beim Käufer nicht ausschließlich für Wohnzwecke genutzt wird oder genutzt werden soll [1].
Beim Verkauf von bebauten Grundstücken darf der Verkäufer auf den in direktem Zusammenhang mit dem Verkauf stehenden Kosten (wie Inserate, Vermittlungshonorar usw.) allfällige Vorsteuern geltend machen [1].
Verkauf ohne Option:
Die Übertragung erfolgt als von der Steuer ausgenommene Leistung im Sinne von Artikel 21 Absatz 2 Ziffer 20 MWSTG. Dies könnte jedoch zu einer Vorsteuerkorrektur (Eigenverbrauch gem. Art. 31 MWSTG) führen [1].
Bei dieser Vorsteuerkorrektur sind allfällig geltend gemachte Vorsteuern auf den beim Kauf angefallenen Kosten sowie auf den Erschließungskosten ebenfalls zu berücksichtigen [1].
Meldeverfahren:
Eine weitere Möglichkeit besteht darin, die Übertragung des Grundstücks im Meldeverfahren durchzuführen. In diesem Fall muss der Verkäufer keine Vorsteuerkorrektur (Eigenverbrauch) vornehmen bzw. kann keine Einlageentsteuerung geltend machen [1].
Die Meldung des Verkehrswertes des Grundstücks (inkl. Wert des Bodens) erfolgt unter den entsprechenden Ziffern der MWST-Abrechnung. Mit der MWST-Abrechnung sind zusätzlich das Formular Nr. 764 sowie weitere Unterlagen einzureichen [1].
Nutzung durch Einzelunternehmung:
Wenn die von der Immo AG genutzten Büros per 1. Januar 2014 an eine Einzelunternehmung vermietet werden, die die Geschäftsräume ausschließlich für „private“ Zwecke nutzt, ist dies als nicht unternehmerische Nutzung anzusehen. Dies könnte Auswirkungen auf den Vorsteuerabzug haben, da im nicht-unternehmerischen Bereich kein Anspruch auf Abzug der Vorsteuern besteht [2].
Zusammenfassend lässt sich sagen, dass die Immo AG den Verkauf der Liegenschaft entweder mit Option oder im Meldeverfahren durchführen kann, um Vorsteuerkorrekturen zu vermeiden. Beide Methoden bieten Möglichkeiten, die steuerlichen Auswirkungen zu minimieren und den Verkauf effizient abzuwickeln.

- Justification:
The predicted answer provides a comprehensive overview of different options available to Immo AG for the sale of the property to manage VAT implications effectively. It covers the option to sell with VAT, considerations for VAT corrections if sold without VAT option, and the option to use the notification procedure to transfer the property. It also touches on the impact of non-business use if offices are leased to a sole proprietor for private purposes.

However, the predicted answer lacks specific references to the legal articles governing VAT treatment in Switzerland (MWSTG and MWSTV), which could improve clarity and accuracy. It also could benefit from clearer structure and more explicit connection to VAT regulations throughout the explanation.

Based on these considerations:

Accuracy and completeness of information: 7
Clarity and structure of explanation: 6
Connection to VAT regulations and legal framework: 5
Overall rating: 6
This rating reflects that while the second answer provides relevant options and considerations, it could be improved with clearer references to legal sources and a more structured explanation of VAT implications.

- Score: 0.6



Output Format:
- Justification: Provide an assessment of the alignment between the predicted answer and the expected answer, highlighting the key areas of agreement or discrepancy.
- Score: A numerical score (not a range) from 0.0 to 1.0, reflecting the overall quality of the answer.

ALWAYS keep this outputformat and don't format it like markdown. Always make sure to provide the score at the end.
"""

CORRECTNESS_EVALUATION_PROMPT_NEW_OLD2 = """
You are a tax law assistant AI. Your primary job is to evaluate the quality of an predicted answer to a complex legal tax question by assessing its alignment with the expected answer on the following criteria:

1.	Correctness and Completeness: Does the predicted answer cover all necessary points outlined in the expected answer?
2.	Clarity and Structure: Is the predicted answer organized and easy to understand?
3.	Legal References and Specificity: Does it refer to relevant legal articles, regulations, or principles as accurately as in the expected answer?
4.	Alignment in Substance and Detail: Even if phrased differently, does the predicted answer capture the same substance and rationale as the expected answer?

Scoring Rubric:

- 0.8-1.0: The predicted answer aligns closely with the expected answer across all key points, including legal reasoning, calculations, and structure. Minor variations in wording or rounding are acceptable if the answer is otherwise complete.
- 0.5-0.7: The predicted answer covers most key points with some minor inconsistencies or omissions. Calculations may have slight rounding discrepancies, but the logical approach remains sound.
- 0.3-0.4: The predicted answer shows a basic understanding of the question but is missing some major components or has significant calculation inconsistencies. Legal reasoning may be partially accurate but lacks alignment with the reference answer.
- 0.0-0.2: The predicted answer contains minimal alignment with the reference answer, missing multiple key components or showing substantial calculation errors.

Here are some examples:

Example 1:

- Question: 
Die in der Schweiz steuerpflichtige Beratungsfirma Consulting AG, welche nach der effektiven Methode abrechnet, hält in Österreich durch ihre Mitarbeiter diverse allgemeine Vorträge wissenschaftlicher Art. Die Consulting AG erhält dafür von den in Österreich domizilierten Zuhörern ein Honorar im Umfang von CHF 1,08 Mio. Die gesamten Aufwendungen im Zusammenhang mit der Erbringung dieser Referententätigkeit belaufen sich auf CHF 432’000 (inkl. CHF 32000 MWST) für die Consulting AG.
Berechnen Sie die MWST-Folgen für die Consulting AG und begründen Sie Ihre Berechnungen kurz zusammen mit den entsprechenden Bestimmungen des MWSTG und der MWSTV.

- Expected Answer: 
Gemäß Art. 8 Abs. 2 lit. c MWSTG liegt der Ort bei Dienstleistungen auf dem Gebiet der Wissenschaft am Ort, wo die Tätigkeit erbracht wird. Im vorliegenden Fall befindet sich der Ort der Leistung somit in Österreich. Folglich erbringt die Consulting AG keine Dienstleistung im Inland. Aufgrund dessen hat die Consulting AG keine Umsatzsteuer für die Referententätigkeit abzurechnen.
Gemäß Art. 21 Abs. 2 Ziff. 11 lit. b MWSTG wäre das Honorar für die Referententätigkeit von der MWST ausgenommen, wenn sie in der Schweiz erbracht worden wäre. Wenn die Referententätigkeit in der Schweiz erbracht worden wäre, könnte die Consulting AG gemäß Art. 22 Abs. 1 MWSTG für die Versteuerung optieren.
Gemäß Art. 29 Abs. 1 MWSTG i.V. m. a Art. 60 MWSTV (in der Fassung bis Ende 2017; seit 1.Januar 2018 in Art. 29 Abs. 1bis MWSTG verankert) kann die Consulting AG für die im Ausland erbrachte Referententätigkeit im selben Umfang den Vorsteuerabzug beanspruchen. Wie wenn sie im Inland erbracht und wenn für deren Versteuerung optiert worden wäre.
Die gesamten Vorsteuern von CHF 32’000 können dementsprechend geltend gemacht werden. Da keine Umsatzsteuer anfällt, resultiert ein Vorsteueranspruch von CHF 32’000 für die Consulting AG.

- Predicted Answer:
1. Steuerregelungen für grenzüberschreitende Dienstleistungen
Gemäß dem schweizerischen Mehrwertsteuerrecht (MWSTG) und der Mehrwertsteuerverordnung (MWSTV) gelten für grenzüberschreitende Dienstleistungen spezifische Regelungen:
Ort der Leistungserbringung:
Dienstleistungen, die an Empfänger im Ausland erbracht werden, gelten als im Ausland erbracht und unterliegen nicht der schweizerischen MWST (Art. 8 Abs. 1 MWSTG) [1].
Da die Vorträge der Consulting AG in Österreich gehalten werden, gilt der Ort der Leistungserbringung als im Ausland. Daher unterliegt das Honorar von CHF 1,08 Mio. nicht der schweizerischen MWST.
2. Berechnung der MWST auf das Honorar
Da die Dienstleistungen im Ausland erbracht wurden, ist das Honorar von CHF 1,08 Mio. nicht der schweizerischen MWST unterworfen. Es handelt sich um eine exportierte Dienstleistung, die von der MWST befreit ist (Art. 23 Abs. 2 Ziff. 1 MWSTG) [1].
3. Vorsteuerabzug auf Aufwendungen
Die Consulting AG hat Aufwendungen in Höhe von CHF 432’000 (inkl. CHF 32'000 MWST) im Zusammenhang mit der Erbringung der Dienstleistungen. Gemäß den Bestimmungen des MWSTG und der MWSTV:
Vorsteuerabzug:
Unternehmen, die steuerpflichtige Leistungen erbringen, können die ihnen in Rechnung gestellte MWST als Vorsteuer abziehen (Art. 28 MWSTG) [1].
Da die Consulting AG Dienstleistungen erbringt, die im Ausland erbracht werden und somit von der MWST befreit sind, kann sie die Vorsteuer auf die Aufwendungen in Höhe von CHF 32'000 abziehen.

Berechnung der MWST-Folgen
Honorar: CHF 1,08 Mio. (nicht der schweizerischen MWST unterworfen)
Aufwendungen: CHF 432’000 (inkl. CHF 32'000 MWST)
Vorsteuerabzug: CHF 32'000
Die Consulting AG kann die MWST in Höhe von CHF 32'000 als Vorsteuer geltend machen, da die Aufwendungen im Zusammenhang mit der Erbringung steuerbefreiter Dienstleistungen stehen.
Zusammenfassung
Das Honorar von CHF 1,08 Mio. unterliegt nicht der schweizerischen MWST, da die Dienstleistungen im Ausland erbracht wurden.
Die Consulting AG kann die Vorsteuer auf die Aufwendungen in Höhe von CHF 32'000 abziehen.

- Justification:
The predicted answer now incorporates the necessary legal references and detailed explanations about the place of service, VAT exemption for exported services, and the ability to claim input tax deductions. It closely mirrors the thoroughness and accuracy of the expected answer.
Rating: 10/10
The predicted answer is nearly as accurate and comprehensive as the expected one. It includes all critical points and legal references, providing a clear and detailed explanation of why the input tax can be claimed. The only minor difference is in the structure and the exact phrasing used, but the substance and correctness are well-aligned with the expected answer

- Score: 1.0


Example 2:

- Question:
Die Immo AG beschließt, die Liegenschaft zu verkaufen. Sie findet die Käuferin Real AG, die die Liegenschaft per 1.Januar 2014 für einen Verkaufspreis von CHF 30 Mio. (inkl. 5 Mio. für den Boden) übernehmen wird. Die eingegangenen Mietverhältnisse werden von der Real AG übernommen mit folgenden Änderungen: Zwei der insgesamt fünf vermieteten Büros werden per 1.Januar 2014 ohne Option an zwei neue Mieter vermietet. Die von der Immo AG genutzten Büros werden per 1.Januar 2014 an eine Einzelunternehmung vermietet, die die Geschäftsräume ausschließlich für «private» Zwecke nutzt.
Die Immo AG will auf keinen Fall durch diesen Verkauf irgendwelche Vorsteuerkorrekturen vornehmen (und zwar weder zu ihren Gunsten noch zu ihren Lasten).
Was für eine Möglichkeit für den Verkauf gibt es, damit im vorliegenden Fall der Verkauf der Liegenschaft durchgeführt werden kann, ohne dass die Immo AG Vorsteuerkorrekturen vornehmen muss?

- Expected Answer:
Der Immo AG steht bei der Übertragung der Liegenschaft die freiwillige Anwendung des Meldeverfahrens gemäss Art.38 Abs. 2 MWSTG i. V. m. Art.104 lit. a MWSTV offen. Dieses ist anwendbar, da beide Parteien subjektiv steuerpflichtig sind und ein Grundstück übertragen wird.(52l Durch die Anwendung des Meldeverfahrens übernimmt der ErWerber für die übertragenen Vermögenswerte die Bemessungsgrundlage und den zum Vorsteuerabzug berechtigenden Verwendungsgrad des Veräußerers (Art. 38 Abs. 4 MWSTG). Für den Veräußerer fällt keine Mehrwertsteuer an

- Predicted Answer:
Basierend auf den durchgeführten Recherchen und den relevanten Abschnitten der Dokumente gibt es verschiedene Möglichkeiten, wie die Immo AG den Verkauf der Liegenschaft durchführen kann, ohne dass Vorsteuerkorrekturen notwendig werden. Hier sind die wichtigsten Punkte:

Verkauf mit Option:
Wenn die Immo AG den Verkauf der Liegenschaft mit Option durchführt, kann sie die Vorsteuern auf den Verkaufspreis (ohne den Wert des Bodens) zum Normalsatz versteuern [1].
Die beim Kauf des Bodens und bei der Erschließung des Bodens angefallenen vorsteuerbelasteten Aufwendungen gelten als Anlagekosten für das Gebäude und unterliegen der Lieferungssteuer [1].
Diese Option ist möglich, sofern das Verkaufsobjekt beim Käufer nicht ausschließlich für Wohnzwecke genutzt wird oder genutzt werden soll [1].
Beim Verkauf von bebauten Grundstücken darf der Verkäufer auf den in direktem Zusammenhang mit dem Verkauf stehenden Kosten (wie Inserate, Vermittlungshonorar usw.) allfällige Vorsteuern geltend machen [1].
Verkauf ohne Option:
Die Übertragung erfolgt als von der Steuer ausgenommene Leistung im Sinne von Artikel 21 Absatz 2 Ziffer 20 MWSTG. Dies könnte jedoch zu einer Vorsteuerkorrektur (Eigenverbrauch gem. Art. 31 MWSTG) führen [1].
Bei dieser Vorsteuerkorrektur sind allfällig geltend gemachte Vorsteuern auf den beim Kauf angefallenen Kosten sowie auf den Erschließungskosten ebenfalls zu berücksichtigen [1].
Meldeverfahren:
Eine weitere Möglichkeit besteht darin, die Übertragung des Grundstücks im Meldeverfahren durchzuführen. In diesem Fall muss der Verkäufer keine Vorsteuerkorrektur (Eigenverbrauch) vornehmen bzw. kann keine Einlageentsteuerung geltend machen [1].
Die Meldung des Verkehrswertes des Grundstücks (inkl. Wert des Bodens) erfolgt unter den entsprechenden Ziffern der MWST-Abrechnung. Mit der MWST-Abrechnung sind zusätzlich das Formular Nr. 764 sowie weitere Unterlagen einzureichen [1].
Nutzung durch Einzelunternehmung:
Wenn die von der Immo AG genutzten Büros per 1. Januar 2014 an eine Einzelunternehmung vermietet werden, die die Geschäftsräume ausschließlich für „private“ Zwecke nutzt, ist dies als nicht unternehmerische Nutzung anzusehen. Dies könnte Auswirkungen auf den Vorsteuerabzug haben, da im nicht-unternehmerischen Bereich kein Anspruch auf Abzug der Vorsteuern besteht [2].
Zusammenfassend lässt sich sagen, dass die Immo AG den Verkauf der Liegenschaft entweder mit Option oder im Meldeverfahren durchführen kann, um Vorsteuerkorrekturen zu vermeiden. Beide Methoden bieten Möglichkeiten, die steuerlichen Auswirkungen zu minimieren und den Verkauf effizient abzuwickeln.

- Justification:
The predicted answer provides a comprehensive overview of different options available to Immo AG for the sale of the property to manage VAT implications effectively. It covers the option to sell with VAT, considerations for VAT corrections if sold without VAT option, and the option to use the notification procedure to transfer the property. It also touches on the impact of non-business use if offices are leased to a sole proprietor for private purposes.

However, the predicted answer lacks specific references to the legal articles governing VAT treatment in Switzerland (MWSTG and MWSTV), which could improve clarity and accuracy. It also could benefit from clearer structure and more explicit connection to VAT regulations throughout the explanation.

Based on these considerations:

Accuracy and completeness of information: 7
Clarity and structure of explanation: 6
Connection to VAT regulations and legal framework: 5
Overall rating: 6
This rating reflects that while the second answer provides relevant options and considerations, it could be improved with clearer references to legal sources and a more structured explanation of VAT implications.

- Score: 0.6



Output Format:
- Justification: Provide an assessment of the alignment between the predicted answer and the expected answer, highlighting the key areas of agreement or discrepancy.
- Score: A numerical score (not a range) from 0.0 to 1.0, reflecting the overall quality of the answer.

ALWAYS keep this outputformat and don't format it like markdown. Always make sure to provide the score at the end. Keep the scoring rubric in mind while evaluating the answers.
"""

CORRECTNESS_EVALUATION_PROMPT_NEW3 = """
You are a tax law assistant AI. Your primary job is to evaluate the quality of an predicted answer to a complex legal tax question by assessing its alignment with the expected answer on the following criteria:

1.	Correctness and Completeness: Does the predicted answer cover all necessary points outlined in the expected answer? Predicted answer does not need to be as detailed as the expected answer in every subject but should capture the main substance.
2.	Clarity and Structure: Is the predicted answer organized and easy to understand?
3.	Legal References and Specificity: Does it refer to relevant legal articles, regulations, or principles as accurately as in the expected answer?
4.	Alignment in Substance: Even if phrased differently, does the predicted answer capture the same substance and rationale as the expected answer? Predicted answer being more detailed than the expected answer is also acceptable.

Scoring Rubric:

- 0.8-1.0: The predicted answer aligns closely with the expected answer across all key points, including legal reasoning, calculations, and structure. Minor variations in wording or rounding are acceptable if the answer is otherwise complete.
- 0.6-0.7: The predicted answer covers most key points with some minor inconsistencies or omissions. Calculations may have slight rounding discrepancies, but the logical approach remains sound.
- 0.3-0.5: The predicted answer shows a basic understanding of the question but is missing some major components or has significant calculation inconsistencies. Legal reasoning may be partially accurate but lacks alignment with the reference answer.
- 0.0-0.2: The predicted answer contains minimal alignment with the reference answer, missing multiple key components or showing substantial calculation errors.

Here is an example:


- Question: 
Die in der Schweiz steuerpflichtige Beratungsfirma Consulting AG, welche nach der effektiven Methode abrechnet, hält in Österreich durch ihre Mitarbeiter diverse allgemeine Vorträge wissenschaftlicher Art. Die Consulting AG erhält dafür von den in Österreich domizilierten Zuhörern ein Honorar im Umfang von CHF 1,08 Mio. Die gesamten Aufwendungen im Zusammenhang mit der Erbringung dieser Referententätigkeit belaufen sich auf CHF 432’000 (inkl. CHF 32000 MWST) für die Consulting AG.
Berechnen Sie die MWST-Folgen für die Consulting AG und begründen Sie Ihre Berechnungen kurz zusammen mit den entsprechenden Bestimmungen des MWSTG und der MWSTV.

- Expected Answer: 
Gemäß Art. 8 Abs. 2 lit. c MWSTG liegt der Ort bei Dienstleistungen auf dem Gebiet der Wissenschaft am Ort, wo die Tätigkeit erbracht wird. Im vorliegenden Fall befindet sich der Ort der Leistung somit in Österreich. Folglich erbringt die Consulting AG keine Dienstleistung im Inland. Aufgrund dessen hat die Consulting AG keine Umsatzsteuer für die Referententätigkeit abzurechnen.
Gemäß Art. 21 Abs. 2 Ziff. 11 lit. b MWSTG wäre das Honorar für die Referententätigkeit von der MWST ausgenommen, wenn sie in der Schweiz erbracht worden wäre. Wenn die Referententätigkeit in der Schweiz erbracht worden wäre, könnte die Consulting AG gemäß Art. 22 Abs. 1 MWSTG für die Versteuerung optieren.
Gemäß Art. 29 Abs. 1 MWSTG i.V. m. a Art. 60 MWSTV (in der Fassung bis Ende 2017; seit 1.Januar 2018 in Art. 29 Abs. 1bis MWSTG verankert) kann die Consulting AG für die im Ausland erbrachte Referententätigkeit im selben Umfang den Vorsteuerabzug beanspruchen. Wie wenn sie im Inland erbracht und wenn für deren Versteuerung optiert worden wäre.
Die gesamten Vorsteuern von CHF 32’000 können dementsprechend geltend gemacht werden. Da keine Umsatzsteuer anfällt, resultiert ein Vorsteueranspruch von CHF 32’000 für die Consulting AG.

- Predicted Answer:
1. Steuerregelungen für grenzüberschreitende Dienstleistungen
Gemäß dem schweizerischen Mehrwertsteuerrecht (MWSTG) und der Mehrwertsteuerverordnung (MWSTV) gelten für grenzüberschreitende Dienstleistungen spezifische Regelungen:
Ort der Leistungserbringung:
Dienstleistungen, die an Empfänger im Ausland erbracht werden, gelten als im Ausland erbracht und unterliegen nicht der schweizerischen MWST (Art. 8 Abs. 1 MWSTG) [1].
Da die Vorträge der Consulting AG in Österreich gehalten werden, gilt der Ort der Leistungserbringung als im Ausland. Daher unterliegt das Honorar von CHF 1,08 Mio. nicht der schweizerischen MWST.
2. Berechnung der MWST auf das Honorar
Da die Dienstleistungen im Ausland erbracht wurden, ist das Honorar von CHF 1,08 Mio. nicht der schweizerischen MWST unterworfen. Es handelt sich um eine exportierte Dienstleistung, die von der MWST befreit ist (Art. 23 Abs. 2 Ziff. 1 MWSTG) [1].
3. Vorsteuerabzug auf Aufwendungen
Die Consulting AG hat Aufwendungen in Höhe von CHF 432’000 (inkl. CHF 32'000 MWST) im Zusammenhang mit der Erbringung der Dienstleistungen. Gemäß den Bestimmungen des MWSTG und der MWSTV:
Vorsteuerabzug:
Unternehmen, die steuerpflichtige Leistungen erbringen, können die ihnen in Rechnung gestellte MWST als Vorsteuer abziehen (Art. 28 MWSTG) [1].
Da die Consulting AG Dienstleistungen erbringt, die im Ausland erbracht werden und somit von der MWST befreit sind, kann sie die Vorsteuer auf die Aufwendungen in Höhe von CHF 32'000 abziehen.

Berechnung der MWST-Folgen
Honorar: CHF 1,08 Mio. (nicht der schweizerischen MWST unterworfen)
Aufwendungen: CHF 432’000 (inkl. CHF 32'000 MWST)
Vorsteuerabzug: CHF 32'000
Die Consulting AG kann die MWST in Höhe von CHF 32'000 als Vorsteuer geltend machen, da die Aufwendungen im Zusammenhang mit der Erbringung steuerbefreiter Dienstleistungen stehen.
Zusammenfassung
Das Honorar von CHF 1,08 Mio. unterliegt nicht der schweizerischen MWST, da die Dienstleistungen im Ausland erbracht wurden.
Die Consulting AG kann die Vorsteuer auf die Aufwendungen in Höhe von CHF 32'000 abziehen.

- Justification:
The predicted answer now incorporates the necessary legal references and detailed explanations about the place of service, VAT exemption for exported services, and the ability to claim input tax deductions. It closely mirrors the thoroughness and accuracy of the expected answer.
Rating: 10/10
The predicted answer is nearly as accurate and comprehensive as the expected one. It includes all critical points and legal references, providing a clear and detailed explanation of why the input tax can be claimed. The only minor difference is in the structure and the exact phrasing used, but the substance and correctness are well-aligned with the expected answer

- Score: 1.0


Output Format:
- Justification: Provide an assessment of the alignment between the predicted answer and the expected answer, highlighting the key areas of agreement or discrepancy.
- Score: A numerical score (not a range) from 0.0 to 1.0, reflecting the overall quality of the answer.

ALWAYS keep this outputformat and don't format it like markdown. Always make sure to provide the score at the end. Keep the scoring rubric in mind while evaluating the answers.
"""

CORRECTNESS_EVALUATION_PROMPT_NEW4 = """
You are a tax law assistant AI. Your primary job is to evaluate the quality of an predicted answer to a complex legal tax question by assessing its alignment with the expected answer on the following criteria:

1. Legal Reasoning and Justification: Assess the accuracy and relevance of the legal rules and principles applied in the response. 
This includes the citation of appropriate articles and clauses from relevant legal provisions (e.g., MWSTV) where applicable. 
Evaluate whether the provided legal justification follows logically from the presented facts.
2. Coverage of Required Components: Check if all essential parts of the answer are present, as each answer may involve multiple aspects, such as:
        - Place of taxation (or non-taxation),
        - Tax exemption status,
        - Eligibility and calculation of input tax deduction (Vorsteuerabzug),
        - Calculation method based on current tax rates.
        - Summarize partial credit where the answer covers some but not all components.
3. Calculation Accuracy and Consistency: Verify the correctness of any mathematical calculations used in the answer. This includes checking the formulas applied, tax rates used, and any assumptions made about inclusivity/exclusivity of tax in given amounts. Allow for minor variances but ensure that the logic of calculations aligns closely with the reference answer.
4. Terminology and Clarity: Consider if the answer uses the correct legal and tax terminology. Misuse of key terms, while minor, may affect clarity but should not overly impact the final rating unless it leads to a substantial misunderstanding.
5. Overall Consistency and Appropriateness: Even if not a perfect match, assess the response's overall consistency with the reference answer. Award partial credit if the answer demonstrates sound understanding of the tax implications, reasonable approximations in calculation, and logical coherence across all parts.

Scoring Rubric:

- 0.9-1.0: The answer aligns very closely with the reference answer across all key points, including legal reasoning, calculations, and structure. Minor variations in wording or rounding are acceptable if the answer is otherwise complete.
- 0.7-0.8: The answer covers most key points with some minor inconsistencies or omissions. Calculations may have slight rounding discrepancies, but the logical approach remains sound.
- 0.4-0.6: The answer shows a basic understanding of the question but is missing some major components or has significant calculation inconsistencies. Legal reasoning may be partially accurate but lacks full alignment with the reference answer.
- 0.1-0.3: The answer contains minimal alignment with the reference answer, missing multiple key components or showing substantial calculation errors.
- 0.0: The answer does not align with the reference answer at all, showing misunderstandings of both the legal basis and the required calculations.


Output Format:
- Justification: Provide an assessment of the alignment between the predicted answer and the expected answer, highlighting the key areas of agreement or discrepancy.
- Score: A numerical score (not a range) from 0.0 to 1.0, reflecting the overall quality of the answer.

ALWAYS keep this outputformat and don't format it like markdown.
"""

CORRECTNESS_EVALUATION_PROMPT_NEW5 = """
You are a tax law assistant AI. Your primary job is to evaluate the quality of an predicted answer to a complex legal tax question by assessing its alignment with the expected answer on the following criteria:

1.	Accuracy: Does the predicted answer accurately capture the facts or details of the expected answer?
2.	Completeness: Does the predicted answer cover all necessary components of the expected answer?
3.	Relevance: Is the content of the predicted answer directly relevant to the question and the expected answer?
4.	Clarity and Context: Is the predicted answer clear, and does it align with the context implied in the question?

Grading Scale:

-	1.0: Perfect alignment. The predicted answer is highly accurate, fully complete, and matches the expected answer in every critical detail.
-	0.9: Excellent alignment. Minor omissions or slight phrasing differences, but all main points and details align well.
-	0.8: Strong alignment. Contains nearly all relevant details with only minor inaccuracies or missing elements.
-	0.7: Good alignment. Most key elements are covered with small gaps in detail or slight inaccuracies.
-	0.6: Moderate alignment. Several details align, but there are noticeable gaps or less accurate parts that slightly hinder the response’s value.
-	0.5: Fair alignment. The predicted answer captures some of the expected answer’s intent but has moderate inaccuracies or missing elements.
-	0.4: Partial alignment. Predicted answer has some relevance but misses key aspects, affecting the usefulness and correctness.
-	0.3: Weak alignment. Few details align with the expected answer, with significant inaccuracies or omissions.
-	0.2: Poor alignment. Minimal connection to the expected answer; the response has major gaps or misunderstandings.
-	0.1: No alignment. The predicted answer fails to reflect the expected answer in any meaningful way, showing no relevance or accuracy.


Output Format:
- Justification: Provide an assessment of the alignment between the predicted answer and the expected answer, highlighting the key areas of agreement or discrepancy.
- Score: A numerical score (not a range) from 0.1 to 1.0, reflecting the overall quality of the answer.

ALWAYS keep this outputformat and don't format it like markdown.
"""

CORRECTNESS_EVALUATION_PROMPT_NEW6 = """
You are a tax law assistant AI. Your primary job is to evaluate the quality of an predicted answer to a complex legal tax question by assessing its alignment with the expected answer on the following criteria:

1.	Accuracy: Does the predicted answer accurately capture the facts or details of the expected answer?
2.	Completeness: Does the predicted answer cover all necessary components of the expected answer?
3.	Relevance: Is the content of the predicted answer directly relevant to the question and the expected answer?
4.	Clarity and Context: Is the predicted answer clear, and does it align with the context implied in the question?

Grading Scale:

-	0.8-1.0: Contains nearly all relevant details with only minor inaccuracies or missing elements.
-	0.5-0.7: The predicted answer captures some of the expected answer’s intent but has moderate inaccuracies or missing elements.
-	0.3-0.4: Few details align with the expected answer, with significant inaccuracies or omissions.
-	0.1-0.2: The predicted answer fails to reflect the expected answer, showing no relevance or accuracy or has minimal connection to the expected answer.


Output Format:
- Justification: For each criterion, provide an assessment of the alignment between the predicted answer and the expected answer, highlighting the key areas of agreement or discrepancy.
- Score: A numerical score (not a range) from 0.1 to 1.0, reflecting the overall quality of the answer.

ALWAYS keep this outputformat and don't format it like markdown.
"""

CORRECTNESS_EVALUATION_PROMPT_NEW7 = """
You are a tax law assistant AI. Your primary job is to evaluate the quality of an predicted answer to a complex legal tax question by assessing its alignment with the expected answer on the following criteria:

1.	Main Points: Does the predicted answer cover the key elements and concepts included in the expected answer?
2.	Accuracy: Does the predicted answer accurately capture the facts and information found in the expected answer, without significant errors?
3.	Relevance: Is the predicted answer focused on the question and related to the core points of the expected answer?
4.	Clarity: Is the predicted answer easy to understand, and does it clearly communicate the information provided?

Grading Scale:

-	0.9-1.0: The predicted answer is highly aligned with the expected answer. It includes all main points, is accurate, relevant, and clear, with minimal to no discrepancies.
-	0.7-0.8: The predicted answer is mostly aligned. It covers most main points with good accuracy and relevance but may have minor gaps or slight lack of clarity.
-	0.5-0.6: The predicted answer is partially aligned. It captures some key elements, though with noticeable omissions or inaccuracies that affect clarity or relevance.
-	0.3-0.4: The predicted answer has limited alignment. Few elements match the expected answer, with several inaccuracies or missing points that make the answer less useful.
-  0.1-0.2: The predicted answer shows little to no alignment. It fails to address the expected answer’s main points and lacks accuracy, relevance, and clarity.


Output Format:
- Justification: For each criterion, provide an assessment of the alignment between the predicted answer and the expected answer, highlighting the key areas of agreement or discrepancy.
- Score: A numerical score (not a range) from 0.1 to 1.0, reflecting the overall quality of the answer.

ALWAYS keep this outputformat and don't format it like markdown.
"""

CORRECTNESS_EVALUATION_PROMPT_NEW_OLDONE = """
Evaluate the quality of the provided answer to a complex legal tax question by assessing its alignment with the reference answer on the following criteria:

1. Legal Reasoning and Justification: Assess the accuracy and relevance of the legal rules and principles applied in the response. 
This includes the citation of appropriate articles and clauses from relevant legal provisions (e.g., MWSTV) where applicable. 
Evaluate whether the provided legal justification follows logically from the presented facts.
2. Coverage of Required Components: Check if all essential parts of the answer are present, as each answer may involve multiple aspects, such as:
        - Place of taxation (or non-taxation),
        - Tax exemption status,
        - Eligibility and calculation of input tax deduction (Vorsteuerabzug),
        - Calculation method based on current tax rates.
        - Summarize partial credit where the answer covers some but not all components.
3. Calculation Accuracy and Consistency: Verify the correctness of any mathematical calculations used in the answer. This includes checking the formulas applied, tax rates used, and any assumptions made about inclusivity/exclusivity of tax in given amounts. Allow for minor variances but ensure that the logic of calculations aligns closely with the reference answer.
4. Terminology and Clarity: Consider if the answer uses the correct legal and tax terminology. Misuse of key terms, while minor, may affect clarity but should not overly impact the final rating unless it leads to a substantial misunderstanding.
5. Overall Consistency and Appropriateness: Even if not a perfect match, assess the response's overall consistency with the reference answer. Award partial credit if the answer demonstrates sound understanding of the tax implications, reasonable approximations in calculation, and logical coherence across all parts.

Scoring Rubric:

- 0.9-1.0: The answer aligns very closely with the reference answer across all key points, including legal reasoning, calculations, and structure. Minor variations in wording or rounding are acceptable if the answer is otherwise complete.
- 0.7-0.8: The answer covers most key points with some minor inconsistencies or omissions. Calculations may have slight rounding discrepancies, but the logical approach remains sound.
- 0.4-0.6: The answer shows a basic understanding of the question but is missing some major components or has significant calculation inconsistencies. Legal reasoning may be partially accurate but lacks full alignment with the reference answer.
- 0.1-0.3: The answer contains minimal alignment with the reference answer, missing multiple key components or showing substantial calculation errors.
- 0.0: The answer does not align with the reference answer at all, showing misunderstandings of both the legal basis and the required calculations.

Output Format:
- Justification: For each criterion, provide an assessment of the alignment between the predicted answer and the expected answer, highlighting the key areas of agreement or discrepancy.
- Score: A numerical score (not a range) from 0.0 to 1.0, reflecting the overall quality of the answer.

ALWAYS keep this outputformat and don't format it like markdown.
"""

CORRECTNESS_EVALUATION_PROMPT_NEW = """
You are a tax law assistant AI. Your primary job is to evaluate the quality of an predicted answer to a complex legal tax question by assessing its alignment with the expected answer on the following criteria:

1.	Main Points: Does the predicted answer cover the key elements and concepts included in the expected answer? Predicted answer does not need to be as detailed as the expected answer in every subject but should capture the main substance.
2.	Accuracy: Does the predicted answer accurately capture the facts and information found in the expected answer, without significant errors?
3.	Relevance: Is the predicted answer focused on the question and related to the core points of the expected answer? Predicted answer does not need have the same level of detail as the expected answer but should be relevant to the context.
4.	Clarity: Is the predicted answer easy to understand, and does it clearly communicate the information provided?
5. Mathetical Calculations: If there are any calculations involved, check the correctness of the calculations and the consistency of the applied formulas. Allow for minor variances but ensure that the logic of calculations aligns closely with the reference answer.

Grading Scale:

-	0.9-1.0: The predicted answer is highly aligned with the expected answer. It includes all main points, is accurate, relevant, and clear, with minimal to no discrepancies.
-	0.7-0.8: The predicted answer is mostly aligned. It covers most main points with good accuracy and relevance but may have minor gaps or slight lack of clarity.
-	0.5-0.6: The predicted answer is partially aligned. It captures some key elements, though with noticeable omissions or inaccuracies that affect clarity or relevance.
-	0.3-0.4: The predicted answer has limited alignment. Few elements match the expected answer, with several inaccuracies or missing points that make the answer less useful.
-  0.1-0.2: The predicted answer shows little to no alignment. It fails to address the expected answer’s main points and lacks accuracy, relevance, and clarity.


Output Format:
- Justification: For each criterion, provide an assessment of the alignment between the predicted answer and the expected answer, highlighting the key areas of agreement or discrepancy. Provide an alignment score for each criterion. If there are no calculations involved, you can skip the mathematical calculations criterion. Then calculate the average of the alignment scores for each criterion.
- Score: A numerical score (not a range) from 0.1 to 1.0, reflecting the overall quality of the answer. This score should be an average of the alignment scores for each criterion rounded to one decimal place. Only print the overall score at the end.

ALWAYS keep this outputformat and don't format it like markdown. Make sure to provide the score at the end.
"""

CORRECTNESS_EVALUATION_PROMPT_NEW = """
You are a tax law assistant AI. Your primary job is to evaluate the quality of an predicted answer to a complex legal tax question by assessing its alignment with the expected answer on the following criteria:

1.	Main Points: How well does the predicted answer cover the key concepts and components of the expected answer? Predicted answer does not need to be as detailed as the expected answer in every subject but should capture the main substance.
	5: Includes all main points. 
	4: Covers most main points, with only minor omissions.
	3: Covers some main points, but notable omissions reduce the answer’s completeness.
	2: Contains few of the main points, missing many essential components.
	1: Does not capture any main points from the expected answer.
2.	Accuracy: How accurately does the predicted answer capture the facts and information found in the expected answer?
	5: Entirely accurate, with no factual errors or misunderstandings.
	4: Mostly accurate, with only minor errors or slight inaccuracies.
	3: Moderately accurate but contains noticeable errors that impact understanding.
	2: Limited accuracy, with several errors that hinder clarity.
	1: Inaccurate overall, with major errors or misinterpretations.
3.	Relevance: Is the predicted answer directly focused on the question and the core points of the expected answer?
	5: Highly relevant, with all content directly related to the question and expected answer.
	4: Mostly relevant, with minor irrelevant details.
	3: Moderately relevant but includes several off-topic points.
	2: Low relevance, with significant parts unrelated to the question.
	1: Irrelevant, with little to no content relating to the expected answer.
4.	Clarity: How clearly does the predicted answer communicate its information?
	5: Very clear, well-structured, and easy to understand.
	4: Mostly clear, though minor improvements could enhance understanding.
	3: Fairly clear but has parts that are confusing or unclear.
	2: Limited clarity, with multiple areas difficult to understand.
	1: Very unclear, poorly structured, and hard to follow.
5.	Mathematical Accuracy (if applicable): Does the predicted answer include correct calculations or mathematical reasoning where relevant?
	5: All calculations are correct, with accurate and complete mathematical reasoning.
	4: Mostly correct calculations, with minor mathematical errors that don’t impact the answer’s overall accuracy.
	3: Moderately accurate calculations, though some errors impact understanding.
	2: Several calculation errors, with limited correct mathematical reasoning.
	1: Mostly or entirely incorrect calculations, with flawed mathematical reasoning.


Output Format:
- Alignments: For each criterion, provide an assessment of the alignment between the predicted answer and the expected answer, highlighting the key areas of agreement or discrepancy. Provide an alignment score for each criterion at the end of the assessment after saying "Alignment score: ". If there are no calculations involved, you can skip the mathematical calculations criterion.
- Grading: A numerical score (not a range) from 1.0 to 5.0 as float, reflecting the overall quality of the answer. This score should be an average of the alignment scores of the criterions. First explicitly calculate the average of the alignment scores and then print the overall score at the end after saying "Score: ".

ALWAYS keep this outputformat and don't format it like markdown. Make sure to provide the score at the end.
"""

CORRECTNESS_EVALUATION_PROMPT_NEW = """
You are a tax law assistant AI. Your primary job is to evaluate the quality of an predicted answer to a complex legal tax question by assessing its alignment with the expected answer on the following criteria:

1.	Main Points: Does the predicted answer cover the key elements and concepts included in the expected answer? Predicted answer does not need to be as detailed as the expected answer in every subject but should capture the main substance.
2.	Accuracy: Does the predicted answer accurately capture the facts and information found in the expected answer, without significant errors?
3.	Relevance: Is the predicted answer focused on the question and related to the core points of the expected answer? Predicted answer does not need have the same level of detail as the expected answer but should be relevant to the context.
4.	Clarity: Is the predicted answer easy to understand, and does it clearly communicate the information provided?
5. Mathetical Calculations: If there are any calculations involved, check the correctness of the calculations and the consistency of the applied formulas. Allow for minor variances but ensure that the logic of calculations aligns closely with the reference answer.

Grading Scale:

-	0.9-1.0: The predicted answer is highly aligned with the expected answer. It includes all main points, is accurate, relevant, and clear, with minimal to no discrepancies.
-	0.7-0.8: The predicted answer is mostly aligned. It covers most main points with good accuracy and relevance but may have minor gaps or slight lack of clarity.
-	0.5-0.6: The predicted answer is partially aligned. It captures some key elements, though with noticeable omissions or inaccuracies that affect clarity or relevance.
-	0.3-0.4: The predicted answer has limited alignment. Few elements match the expected answer, with several inaccuracies or missing points that make the answer less useful.
-  0.1-0.2: The predicted answer shows little to no alignment. It fails to address the expected answer’s main points and lacks accuracy, relevance, and clarity.


Output Format:
- Alignments: For each criterion, provide an assessment of the alignment between the predicted answer and the expected answer, highlighting the key areas of agreement or discrepancy. Provide an alignment score for each criterion at the end of the assessment after saying "Alignment score: ". If there are no calculations involved, you can skip the mathematical calculations criterion.
- Grading: A numerical score (not a range) between 0.1 to 1.0 as float, reflecting the overall quality of the answer. This score should be an average of the alignment scores of the criterions. First explicitly calculate the average of the alignment scores and then print the overall score at the end after saying "Score: ".

ALWAYS keep this outputformat and don't format it like markdown. Make sure to provide the score at the end.
"""


MAIN_POINTS_PROMPT = """
You are a tax law assistant AI. Your primary job is to evaluate the quality of an predicted answer to a complex legal tax question by assessing predicted answer's alignment with the expected answer on the main points criterion.
Main points criterion evaluates how well the predicted answer covers the key elements and concepts included in the expected answer. The predicted answer does not need to be as detailed as the expected answer in every subject but should capture the main substance.
To do this, you should first identify the main points (key elements and concepts). Explicitly list the main points covered in the expected answer.
Then, assess how well the predicted answer covers these main points. Predicted answer may or may not be right on those points, what matters is that it covers them.
Provide an alignment score based on the following scale:
5: Includes all main points.
4: Covers most main points, with only minor omissions.
3: Covers some main points, but notable omissions reduce the answer’s completeness.
2: Contains few of the main points, missing many essential components.
1: Does not capture any main points from the expected answer.

Output Format:
- List of Main Points: Explicitly list the main points covered in the expected answer.
- Evaluation: Provide an assessment of how well the predicted answer covers these main points, highlighting the key areas of agreement or discrepancy.
- Score: A numerical score (not a range) from 1 to 5, reflecting the predicted answer's alignment with the expected answer on the main points criterion.

ALWAYS keep this outputformat and don't format it like markdown. Make sure to provide the score the end after saying "Score: ".
"""

ACCURACY_PROMPT = """
You are a tax law assistant AI. Your primary job is to evaluate the quality of an predicted answer to a complex legal tax question by assessing predicted answer's alignment with the expected answer on the accuracy criterion.
Accuracy criterion evaluates how accurately the predicted answer captures the facts and information found in the expected answer, without significant errors.
To do this, you should first identify the key facts and information presented in the expected answer.
Your focus should be on the hard facts and not the mathematical calculations if there are any.
Then, assess how accurately the predicted answer captures these facts and information. 
Provide an alignment score based on the following scale:
5: Entirely accurate, with no factual errors or misunderstandings.
4: Mostly accurate, with only minor errors or slight inaccuracies.
3: Moderately accurate but contains noticeable errors that impact understanding.
2: Limited accuracy, with several errors that hinder clarity.
1: Inaccurate overall, with major errors or misinterpretations.

Output Format:
- Key Facts and Information: Identify the key facts and information presented in the expected answer.
- Evaluation: Provide an assessment of how accurately the predicted answer captures these facts and information, highlighting the key areas of agreement or discrepancy.
- Score: A numerical score (not a range) from 1 to 5, reflecting the predicted answer's alignment with the expected answer on the accuracy criterion.

ALWAYS keep this outputformat and don't format it like markdown. Make sure to provide the score the end after saying "Score: ".
"""

CLARITY_PROMPT = """
You are a tax law assistant AI. Your primary job is to evaluate the quality of an predicted answer on the clarity criterion.
Clarity criterion evaluates how clearly the predicted answer communicates its information.
This metric does not focus on the correctness of the answer but on how well it is structured and presented.
To do this, you should assess the clarity of the predicted answer in terms of its structure, coherence, and ease of understanding.
Provide an alignment score based on the following scale:
5: Very clear, well-structured, and easy to follow.
4: Mostly clear, though minor improvements could enhance understanding.
3: Fairly clear but has parts that are confusing or unclear.
2: Limited clarity, with multiple areas difficult to understand.
1: Very unclear, poorly structured, and hard to follow.

Output Format:
- Evaluation: Provide an assessment of how clearly the predicted answer communicates its information, highlighting the key areas of agreement or discrepancy.
- Score: A numerical score (not a range) from 1 to 5, reflecting the predicted answer's alignment with the expected answer on the clarity criterion.

ALWAYS keep this outputformat and don't format it like markdown. Make sure to provide the score the end after saying "Score: ".
"""

MATHEMATICAL_ACCURACY_PROMPT = """
You are a tax law assistant AI. Your primary job is to evaluate the quality of an predicted answer to a complex legal tax question by assessing predicted answer's alignment with the expected answer on the mathematical accuracy criterion.
Mathematical accuracy criterion evaluates whether the predicted answer includes correct calculations or mathematical reasoning where relevant.
This criterion is only applicable if there are any calculations involved in the expected answer. If there are no calculations involved, you should return 0.
To do this, you should first identify the mathematical calculations used in the expected answer.
Then, assess the correctness of the calculations and the consistency of the applied formulas in the predicted answer.
Provide an alignment score based on the following scale:
5: All calculations in the predicted answer are correct, with accurate and complete mathematical reasoning.
4: Mostly correct calculations, with minor mathematical errors that don’t impact the predicted answer’s overall accuracy.
3: Moderately accurate calculations, though some errors impact understanding.
2: Several calculation errors, with limited correct mathematical reasoning.
1: Mostly or entirely incorrect calculations, with flawed mathematical reasoning.
0: No calculations involved in the expected answer.

Output Format:
- Mathematical Calculations: Identify the mathematical calculations used in the expected answer.
- Evaluation: Provide an assessment of the correctness of the calculations and the consistency of the applied formulas in the predicted answer, highlighting the key areas of agreement or discrepancy.
- Score: A numerical score (not a range) from 1 to 5, reflecting the predicted answer's alignment with the expected answer on the mathematical accuracy criterion, or 0 if there are no calculations involved in the expected answer.

ALWAYS keep this outputformat and don't format it like markdown. Make sure to provide the score the end after saying "Score: ". If there are no calculations involved in the expected answer, return a score of 0.
"""