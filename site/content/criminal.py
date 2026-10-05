"""Criminal defense hub and spokes. The DUI page exists but is linked only from this hub and its siblings,
never from the global navigation, footer or home page (client instruction)."""
from .base import page, A, ext, img, p, ul, checks, steps, callout, answer, band, esc, table
from . import firm
from .local import cite, link

HUB = "criminal-defense"
TEL = f'<a href="tel:{firm.PHONE_E164}">{firm.PHONE}</a>'


def sp(slug, **kw):
    kw.setdefault("kind", "spoke")
    kw.setdefault("hub", HUB)
    kw.setdefault("eyebrow", "Criminal defense · Summerville, SC")
    return page(slug, **kw)


hub_body = (
    '<h2>Defense from someone who built cases for fourteen years</h2>'
    '<p>Jack Frost was a Summerville police officer and a Charleston County Sheriff\'s Office detective, narcotics investigator and SWAT operator before he became a lawyer. He has written the warrants, run the surveillance, handled the informants and testified in the courtrooms where he now defends clients. That background is not a slogan; it is how he finds the weak point in a case.</p>'
    '<p>We handle charges in the magistrate and municipal courts of Summerville, Dorchester, Berkeley and Charleston counties and in General Sessions (circuit) court, for adults and, in appropriate cases, juveniles and young adults facing their first charge.</p>'
    '<h2>Charges we defend</h2>'
    '[[cards:drug-charges,domestic-violence-defense,dui-lawyer-summerville-sc,traffic-tickets]]'
    '<h2>Getting out, getting ahead, and cleaning up</h2>'
    '[[cards:bond-hearings,arrest-warrants,expungements]]'
    '<p>We also defend assault and battery, shoplifting and other theft charges, disorderly conduct and open container cases, weapons charges, and probation violations. If your charge is not listed, call—if we cannot take it, we will tell you who should.</p>'
    '<h2>What to do right now</h2>'
    + steps([
        ("Stop talking about the case.", " Not to the officer, not to the “victim,” not on social media, not on a recorded jail phone. Everything you say is evidence, and a friendly conversation is the most common way a case gets finished."),
        ("Write down what happened.", " Times, places, names, what was said and by whom—while it is fresh. Keep it for your lawyer only."),
        ("Keep every piece of paper.", " The ticket, the bond paperwork, the incident report number, the court date. Photograph them."),
        ("Call before the first court date.", " Bond conditions, a no-contact order, or a missed date can create new problems before the original charge is even addressed."),
    ]) +
    '<h2>How a South Carolina criminal case moves</h2>'
    + steps([
        ("Arrest or citation.", " A uniform traffic ticket or a warrant. Some charges start with a courtesy summons rather than an arrest."),
        ("Bond hearing.", f" Usually within 24 hours of a warrant arrest, before a magistrate or municipal judge. {A('bond-hearings', 'What happens at a bond hearing')}."),
        ("Which court.", " Magistrate and municipal courts handle most misdemeanors with penalties up to 30 days in jail (and specific offenses the legislature assigned to them, such as third-degree domestic violence). Everything heavier goes to General Sessions."),
        ("Discovery and investigation.", " We obtain the incident report, body-camera and dash-camera video, lab results and witness statements—and we investigate on our own."),
        ("Resolution.", " Dismissal, diversion (pretrial intervention, conditional discharge, traffic education), a negotiated plea to a lesser charge, or trial. Most cases resolve before trial; the ones that do not are prepared as if they will."),
    ]) +
    '<h2>Why clients choose Jack</h2>'
    + checks(["He reads reports and video the way the officer wrote and recorded them, and sees what is missing.",
              "He knows the prosecutors, officers and judges in Dorchester, Berkeley and Charleston counties, which makes negotiation faster and calmer.",
              "He is direct about the likely outcomes and the cost, and he returns calls.",
              "A conviction follows you for employment, housing, licensing and immigration; his goal from day one is the resolution that leaves the smallest mark."]) +
    band("Facing charges? Let's talk today.", "A prompt consultation can make all the difference. Call before you answer anyone else's questions.")
)
page(HUB, kind="hub", section_label="Criminal defense services",
     title="Criminal Defense Attorney in Summerville, SC | Former Detective Jack Frost",
     description="Summerville, SC criminal defense attorney Jack Frost spent 14 years in law enforcement before law school. Drug charges, domestic violence, bond hearings, warrants, traffic offenses and expungements in Dorchester, Berkeley and Charleston counties.",
     h1="Criminal Defense Attorney in Summerville, SC", eyebrow="Protecting your future", nav_label="Criminal defense", hero_image="client-meeting.jpg", hero_caption="Jack and Tara Frost with a client",
     lead="Experienced, discreet defense from an attorney who understands both sides of the justice system. The sooner you call, the more options you have.",
     summary="Drug charges, domestic violence, bond, warrants, traffic and expungements.",
     body=hub_body, priority=0.9,
     faqs=[
         ("Should I talk to the police to clear things up?", "Not without a lawyer. You have the right to remain silent and to counsel; using both is the single best decision most people can make in the first 48 hours."),
         ("What will my case cost?", "Most misdemeanors are quoted as a flat fee after we hear the facts; felonies and trials are quoted in stages. We tell you the number before you hire us."),
         ("Do you handle cases in Berkeley and Charleston counties?", "Yes—magistrate, municipal and General Sessions courts in all three counties."),
     ])

# ----------------------------------------------------------------------------- DUI (linked from hub and siblings only)
sp("dui-lawyer-summerville-sc", card_new=True,
   title="First-Offense DUI in South Carolina | Penalties, License & Defense | Summerville DUI Lawyer",
   description="What a first-offense DUI in South Carolina costs under S.C. Code § 56-5-2930: fines by breath result, 48 hours to 90 days, the six-month suspension, ADSAP, and the ignition interlock every conviction now requires. Summerville DUI lawyer Jack Frost.",
   h1="First-Offense DUI in South Carolina: Penalties, Your License and the Defense", nav_label="DUI &amp; DUAC defense",
   lead="Two clocks start the night you are charged: the criminal case and your driver's license. A former officer who has made these arrests, and who now prosecutes them for the Town of Summerville, explains both.",
   summary="First-offense penalties by breath result, the 2024 interlock rule, the 30-day license deadline and the defenses that work.",
   body=(
       answer("A first-offense DUI in South Carolina is a misdemeanor under S.C. Code § 56-5-2930. The penalty depends on your breath or blood result: a $400 fine or 48 hours to 30 days in jail below 0.10; $500 or 72 hours to 30 days from 0.10 to 0.15; and $1,000 or 30 to 90 days at 0.16 and above. A conviction also brings a six-month license suspension, the ADSAP program and, since May 19, 2024, an ignition interlock device for six months for every first offender. DUI cannot be expunged and is not eligible for pretrial intervention. The license side of the case has its own 30-day deadline.", "The short answer")
       + '<h2>DUI and DUAC: what the State has to prove</h2>'
       f'<p>DUI ({cite("dui", "S.C. Code § 56-5-2930")}) requires proof that your faculties to drive were “materially and appreciably impaired” by alcohol, drugs or both. DUAC ({cite("duac", "§ 56-5-2933")}) is the per-se offense: a breath or blood alcohol concentration of 0.08 or more measured within two hours of arrest, with no need to prove impairment. The penalties are identical, the State chooses which charge to pursue, and you cannot be convicted of both for one stop. Jack Frost made these arrests for fourteen years and now prosecutes them for the Town of Summerville, so he knows what the officer must document and where the documentation usually fails.</p>'
       '<h2>First-offense penalties under § 56-5-2930</h2>'
       + table(["Breath or blood result", "Fine", "Jail, or public service in place of the minimum"], [
           ["Under 0.10", "$400", "48 hours to 30 days"],
           ["0.10 to 0.15", "$500", "72 hours to 30 days"],
           ["0.16 or higher", "$1,000", "30 to 90 days"],
       ]) +
       '<p>The fine cannot be suspended, and with court assessments and surcharges a $400 fine comes to roughly $992 by the time it is paid, according to the Department of Public Safety. The judge may allow public-service hours in place of the minimum jail time but cannot be forced to. Only prior DUI or DUAC offenses within the previous ten years count toward a second or third offense. A first offense is tried in magistrate or municipal court, where you have the right to a jury.</p>'
       '<h2>Everything else a conviction brings</h2>'
       + checks([
           "<b>A six-month driver's license suspension</b>, separate from any administrative suspension for a refusal or a high reading.",
           "<b>ADSAP.</b> Every DUI conviction requires enrollment in the Alcohol and Drug Safety Action Program within 30 days. The statute caps the cost at $500 for education, $2,000 for treatment and $2,500 in total, and the court can hold you in contempt for not enrolling.",
           f"<b>An ignition interlock device for six months.</b> Act 55 of 2023 made South Carolina an all-offender interlock state on May 19, 2024. Under {ext('https://www.scstatehouse.gov/code/t56c005.php', 'S.C. Code § 56-5-2941')} a first offender needs the device for six months to regain driving privileges, a second offender for two years, a third for three years (four if the third offense falls within five years of the first), and a fourth offender for life. You pay a state-approved vendor to install, monitor and remove it, and the device will not start the car at 0.02 or above. Most websites still describe the old rule, under which first offenders below 0.15 avoided the device; that rule is gone.",
           "<b>Insurance.</b> An SR-22 filing for three years and premiums that commonly double or triple.",
           f"<b>A permanent record.</b> DUI and DUAC are excluded from expungement ({cite('expungement_misdemeanor', 'S.C. Code § 22-5-910')}) and from pretrial intervention ({cite('pti', '§ 17-22-50')}). There is no waiting period after which it comes off.",
           "<b>Professional consequences</b> for CDL holders, nurses, teachers, pilots, service members at Joint Base Charleston and anyone who holds a security clearance or a concealed-weapons permit."]) +
       '<h2>The license track: implied consent and the 30-day deadline</h2>'
       f'<p>If you refused the breath test or registered 0.15 or higher, the officer took your license on the spot under the implied-consent law ({cite("implied_consent", "S.C. Code §§ 56-5-2950 and 56-5-2951")}). You have <b>30 days</b> to request a hearing before the Office of Motor Vehicle Hearings, and a timely request usually comes with a temporary alcohol license that lets you keep driving while you wait. The hearing is often the first chance to question the arresting officer under oath, and what the officer says there is locked in for the criminal case. Miss the deadline and the suspension simply stands. If the suspension later takes effect, the interlock-restricted license is now the route back to lawful driving.</p>'
       '<h2>The video rule, and when a case is dismissed</h2>'
       f'<p>South Carolina\'s DUI video statute ({cite("dui_video", "S.C. Code § 56-5-2953")}) requires the stop to be recorded from the moment the blue lights come on through the field sobriety tests, the arrest and the reading of your rights, and requires video of the breath-test room showing the twenty-minute observation period and the test itself. The statute allows only four narrow excuses, each of which the officer must support with a sworn affidavit. Under <em>City of Rock Hill v. Suchenski</em> (2007), an inexcusable failure to record the required parts of the stop requires dismissal, and you do not have to prove the missing footage would have helped you. In <em>State v. Taylor</em> (2022) the Supreme Court narrowed one piece of that rule: when only the Miranda warning is missing from the recording, the remedy is suppression of your statements rather than dismissal of the case. Jack reviews every minute of video against the officer\'s report because he knows exactly what the recording is supposed to show.</p>'
       '<h2>Second, third and felony DUI</h2>'
       '<p>Penalties climb steeply. A second offense within ten years carries a fine of $2,100 to $5,100 and five days to one year in jail at the lowest reading, rising to $3,500 to $6,500 and 90 days to three years at 0.16 or more, with a two-year interlock period. A third offense starts at $3,800 to $6,300 and 60 days to three years and tops out at $7,500 to $10,000 and six months to five years. A fourth offense is a felony punishable by one to seven years. Felony DUI, charged when a crash causes great bodily injury or death, carries 30 days to 15 years and $5,100 to $10,100 in fines for injury, and one to 25 years and $10,100 to $25,100 for a death. Second and subsequent offenses are heard in General Sessions court.</p>'
       '<h2>How these cases are defended</h2>'
       + checks(["<b>The stop.</b> Was there a lawful reason to pull you over? A stop without reasonable suspicion suppresses everything after it, including a checkpoint that did not follow the required procedures.",
                 "<b>The field sobriety tests.</b> Were they administered and scored as the officer was trained, on video, on a suitable surface, with your medical conditions and footwear taken into account?",
                 "<b>The breath test.</b> The twenty-minute observation period, the machine's maintenance and calibration records, the operator's certification and the required video of the test room.",
                 "<b>Blood draws.</b> The warrant, the chain of custody and the lab's procedures.",
                 "<b>The video.</b> What it shows, what it does not, and whether the statute's requirements and affidavits were met.",
                 "<b>The paperwork.</b> Implied-consent advisements, the ticket itself and the officer's report, compared line by line to the video.",
                 "<b>The negotiation.</b> Where the evidence has problems, a reduction to reckless driving or another non-DUI resolution avoids the interlock, ADSAP and the permanent record. No lawyer can promise one; the facts and the video decide."]) +
       '<h2>Court, and one case we cannot take</h2>'
       '<p>First-offense DUI charges from Dorchester or Berkeley County sheriff\'s deputies and the Highway Patrol are tried in the county magistrate\'s court, and charges from a town police department in that town\'s municipal court, with a right to a jury trial in each. Higher offenses go to General Sessions. One exception: Jack serves as the Town of Summerville\'s DUI prosecutor, so the firm does not defend DUI charges brought by the Summerville Police Department in Summerville Municipal Court. If that is your case, call anyway and we will refer you to a defense attorney we trust.</p>'
       + callout("<b>Frost first:</b> if you have not yet requested the administrative hearing, that is the first call. The criminal case can wait a day; the license deadline cannot.")
       + band("Charged with DUI in Dorchester, Berkeley or Charleston County?", "Call today. The 30-day license clock is already running.")
   ),
   faqs=[
       ("What is the penalty for a first-offense DUI in South Carolina?", "A fine of $400 to $1,000 or 48 hours to 90 days in jail depending on the breath result, a six-month license suspension, the ADSAP program and, since May 2024, an ignition interlock device for six months. With assessments the $400 fine is close to $1,000."),
       ("Do I need an ignition interlock for a first DUI in South Carolina?", "Yes. Since May 19, 2024, South Carolina requires the device for nearly every DUI or DUAC conviction, including a first offense with a reading under 0.15. The first-offense period is six months, and you pay the vendor's installation and monthly fees."),
       ("Will I lose my license after a first DUI?", "A conviction brings a six-month suspension. A refusal or a reading of 0.15 or higher triggers a separate administrative suspension the night of the arrest, which you can contest within 30 days."),
       ("Can a first-offense DUI be reduced to reckless driving?", "Sometimes, particularly when the video, the stop or the breath test has problems. Reckless driving carries six points and a fine but none of the DUI consequences. Whether a reduction is realistic depends on the evidence, and no lawyer can promise one."),
       ("Can a DUI be expunged in South Carolina?", "No. DUI and DUAC convictions are excluded from expungement, which is one reason the defense matters so much."),
       ("Do I have to take the breath test?", "You can refuse, but refusal triggers an administrative suspension and can be used at trial. Whether it helped or hurt depends on facts we will review with you."),
       ("How long does a first-offense DUI case take in Dorchester County?", "Most magistrate and municipal court cases resolve within three to six months; a jury trial can take longer. The license hearing runs on its own schedule."),
   ],
   related=["traffic-tickets", "bond-hearings", "expungements"])

sp("drug-charges",
   title="Drug Charge Lawyer in Summerville, SC | Possession, PWID & Trafficking Defense",
   description="Simple possession, possession with intent to distribute and trafficking charges in Dorchester, Berkeley and Charleston counties, defended by former narcotics detective Jack Frost. Conditional discharge, PTI and suppression explained.",
   h1="Drug Charges in Summerville, SC", nav_label="Drug charges",
   lead="Jack Frost investigated narcotics cases for years before he defended them. Here is how South Carolina drug charges work and where they fall apart.",
   summary="Possession, PWID and trafficking, from a former narcotics detective.",
   body=(
       '<h2>The three levels</h2>'
       + table(["Charge", "What it means", "Where it is tried"], [
           ["Simple possession", "A personal-use amount—for marijuana, one ounce or less on a first offense", "Magistrate or municipal court (first offense)"],
           ["Possession with intent to distribute (PWID)", "A larger amount, or possession with packaging, scales, cash or messages suggesting sale; an amount over the statutory threshold is prima facie evidence of intent", "General Sessions"],
           ["Trafficking", "Possession of a quantity at or above the trafficking threshold, regardless of intent to sell—with mandatory minimum sentences", "General Sessions"],
       ]) +
       f'<p>The controlling statute is {cite("drugs", "S.C. Code § 44-53-370")}; penalties depend on the drug schedule, the weight, and prior convictions. Proximity to a school or park adds a separate charge.</p>'
       '<h2>First offense? There may be a way out</h2>'
       f'<p>For a first simple-possession charge, South Carolina\'s conditional discharge statute ({cite("conditional_discharge", "S.C. Code § 44-53-450")}) allows the court to defer proceedings and dismiss the charge after a period of probation-style conditions—leaving no conviction and, after the waiting period, an expungeable record. Pretrial intervention ({cite("pti", "S.C. Code § 17-22-10 et seq.")}) is available for many first-time offenders facing more serious charges, with dismissal on completion. Jack knows which prosecutors offer which programs and when to ask.</p>'
       '<h2>Where drug cases fall apart</h2>'
       + checks(["<b>The search.</b> A traffic stop stretched into a search without consent, probable cause or a warrant; a “knock and talk” that became an entry; a K-9 sniff that extended the stop unlawfully.",
                 "<b>Possession itself.</b> Drugs in a shared car or house belong to nobody until the State proves knowledge and control. Constructive-possession cases are among the weakest prosecutors bring.",
                 "<b>The weight.</b> Trafficking thresholds are exact; packaging, moisture and lab method matter.",
                 "<b>Informants and controlled buys.</b> Reliability, corroboration and whether the warrant affidavit told the whole truth—Jack has written these affidavits and knows how they are supposed to read.",
                 "<b>Chain of custody and the lab.</b> Every hand the evidence passed through, documented."]) +
       '<h2>Collateral consequences</h2>'
       '<p>A drug conviction can cost federal student aid, a professional license, public housing, immigration status and a security clearance. Diversion and reduced charges are usually worth more than the sentence itself, and we plan the defense around what you stand to lose.</p>'
       + band("Drug charge in Dorchester, Berkeley or Charleston County?", "Say nothing to investigators. Call Jack, and bring every piece of paper you were given.")
   ),
   faqs=[
       ("Is marijuana legal in South Carolina?", "No. Possession of any amount remains a crime, though first-offense simple possession is a magistrate-level misdemeanor with diversion options."),
       ("They found drugs in my car but they weren't mine.", "That is a constructive-possession case, and the State must prove you knew about the drugs and had control over them. These cases are very defensible."),
       ("Can a drug charge be expunged?", f"Many first-offense simple-possession dispositions can, after the waiting period, and dismissed charges are expunged automatically or on request. See {A('expungements', 'expungements')}."),
   ],
   related=["bond-hearings", "expungements", "arrest-warrants"])

sp("domestic-violence-defense",
   title="Domestic Violence 3rd Degree in South Carolina | Degrees, Penalties & Defense | Summerville CDV Lawyer",
   description="The three degrees of domestic violence under S.C. Code § 16-25-20: third degree (up to 90 days), second degree (up to 3 years), first degree (up to 10 years) and DVHAN, plus bond conditions, the firearm ban and how CDV cases are defended in Dorchester, Berkeley and Charleston counties.",
   h1="Domestic Violence Charges in South Carolina: Third, Second and First Degree", nav_label="Domestic violence (CDV)",
   lead="A domestic violence arrest happens fast, often on one person's word, the same night. What follows is slower, and it can be defended.",
   summary="Degrees and penalties, bond conditions, the firearm ban, expungement and the defense of CDV charges.",
   body=(
       answer("Domestic violence in the third degree is the most common charge. It is a misdemeanor under S.C. Code § 16-25-20(D) punishable by a fine of $1,000 to $2,500, up to 90 days in jail, or both, and it is usually tried in magistrate or municipal court. Second degree carries up to three years and a fine of $2,500 to $5,000; first degree is a felony with up to ten years; domestic violence of a high and aggravated nature carries up to twenty. Any conviction brings a federal lifetime firearm ban. A first-offense third-degree conviction can be expunged after five years, and many first-time cases qualify for pretrial intervention.", "The short answer")
       + '<h2>Who counts as a household member</h2>'
       f'<p>South Carolina\'s domestic violence statute ({cite("cdv", "S.C. Code § 16-25-20")}) applies only to “household members”: spouses and former spouses, people who have a child in common, and a man and woman who live together or have lived together. An argument with a roommate of the same sex, a sibling or a dating partner you have never lived with is charged as assault, not domestic violence, and the difference matters because the domestic violence label carries the firearm ban and the longer expungement wait. The offense itself is causing physical harm to a household member, or offering or attempting to cause harm with the apparent present ability to do so, in a way that creates fear of imminent peril.</p>'
       '<h2>The three degrees, and what moves a case up</h2>'
       + table(["Charge", "Court", "Penalty", "What puts a case in this degree"], [
           ["Third degree, § 16-25-20(D)", "Magistrate or municipal court (or General Sessions at the solicitor's election)", "Misdemeanor: $1,000 to $2,500 fine, up to 90 days, or both", "The basic offense with none of the aggravating facts below"],
           ["Second degree, § 16-25-20(C)", "General Sessions", "Misdemeanor: $2,500 to $5,000 fine, up to 3 years, or both", "Moderate bodily injury or the likelihood of it; a prior domestic violence conviction within ten years; violating a protective order; committing the act in front of a minor, against a pregnant woman, during a robbery, burglary, kidnapping or theft, or by impeding breathing or circulation"],
           ["First degree, § 16-25-20(B)", "General Sessions", "Felony: up to 10 years", "Great bodily injury or the likelihood of it; two or more prior convictions within ten years; use of a firearm; or a second-degree aggravator committed while a protective order is in place"],
           ["High and aggravated nature, § 16-25-65", "General Sessions", "Felony: up to 20 years", "Extreme indifference to human life, great bodily injury, or an offense committed with a deadly weapon or while a protective order is in place"],
       ]) +
       '<p>Assault and battery in the third degree is a lesser-included offense of domestic violence in the third degree, which is one reason the facts in the incident report matter so much: the same shove can be charged three different ways.</p>'
       '<h2>What happens the first week</h2>'
       + steps([("Arrest.", " Officers responding to a domestic call are trained to identify a primary aggressor and make an arrest. It is not unusual for the person who called 911 to be the one arrested."),
                ("Bond hearing within 24 hours.", " In Dorchester County, bond court sits at the Summerville magistrate's office at 9 a.m. and 3 p.m. every day, including weekends. The judge will almost always impose a no-contact condition covering the other person and often the shared home. Violating it, even by answering a text the other person sent, is a new charge and a revoked bond."),
                ("Living arrangements.", " You may need a police escort to retrieve belongings. We handle the requests to modify bond conditions when the family wants contact restored, and judges grant them far more readily when counsel presents a plan."),
                ("The case.", " The State, not the alleged victim, decides whether to prosecute; a request to “drop the charges” does not end the case. Evidence comes from the 911 recording, body-camera video, photographs, medical records and statements, and third-degree cases in magistrate court often move to a bench or jury trial within a few months.")]) +
       '<h2>Consequences beyond the sentence</h2>'
       f'<p>Any domestic violence conviction, including third degree, triggers the federal lifetime prohibition on possessing firearms and ammunition for a misdemeanor crime of domestic violence. South Carolina adds its own prohibition ({ext("https://www.scstatehouse.gov/code/t16c025.php", "S.C. Code § 16-25-30")}), whose length depends on the degree, and the judge must warn you about it at sentencing. For a hunter, a police officer, a service member or anyone with a concealed-weapons permit, that alone changes the calculus. Convictions also surface in custody cases, security-clearance reviews, immigration proceedings and employment background checks, and a domestic violence conviction waits five years for expungement rather than three.</p>'
       '<h2>How these cases are defended</h2>'
       + checks(["<b>Self-defense and defense of others.</b> South Carolina law protects the person who was actually attacked, and the first person to call 911 is not always that person.",
                 "<b>The body-camera video</b> often tells a different story than the incident report. Jack reviews every minute, because he wrote reports like these for fourteen years.",
                 "<b>Inconsistent statements</b> between the 911 call, the scene interview, the written statement and later testimony.",
                 "<b>Injuries</b> that do not match the description, or none at all, and photographs taken hours later that show something different.",
                 "<b>The household-member element.</b> If the relationship does not fit the statute, the charge is not domestic violence.",
                 "<b>Pretrial intervention.</b> First-time third-degree cases are often eligible; completing the program ends in a dismissal and an expungement rather than a conviction.",
                 "<b>Negotiated outcomes</b> that avoid the domestic violence label, such as a plea to a non-domestic offense, when the evidence supports one."]) +
       '<h2>Where these cases are heard</h2>'
       '<p>Third-degree charges from the Dorchester County Sheriff\'s Office are heard at the Summerville magistrate\'s court at 212 Deming Way; charges from the Summerville Police Department go to Summerville Municipal Court; Berkeley and Charleston County cases go to their magistrate and municipal courts. Second-degree and higher charges go to General Sessions in St. George, Moncks Corner or Charleston. Jack appears in all of them.</p>'
       + callout("<b>Frost first:</b> do not contact the other person to “work it out,” even if they reach out first. Call us; we will address the no-contact order through the court.")
       + band("Arrested for domestic violence?", "Call before the bond hearing if you can, and before you talk to anyone if you cannot.")
   ),
   faqs=[
       ("What is the penalty for domestic violence 3rd degree in South Carolina?", "A fine of $1,000 to $2,500, up to 90 days in jail, or both. It is a misdemeanor, usually heard in magistrate or municipal court, and it carries a federal firearm ban and a five-year wait for expungement."),
       ("Can the victim drop domestic violence charges in South Carolina?", "No. Only the prosecutor can dismiss a charge. The alleged victim's wishes matter, but the State decides."),
       ("Can I go home after a CDV arrest?", "Not if the bond order says no contact with the other person or the residence. We can ask the court to modify the conditions once things have settled."),
       ("Is domestic violence 3rd degree a felony in SC?", "No. Third and second degree are misdemeanors, although second degree carries up to three years. First degree and domestic violence of a high and aggravated nature are felonies."),
       ("Can third-degree domestic violence be expunged?", "A first-offense third-degree conviction can be expunged after five years with no other convictions. A charge dismissed through pretrial intervention or otherwise can be expunged as soon as the case is closed."),
       ("Will I lose my gun rights after a domestic violence conviction?", "Yes. Federal law imposes a lifetime ban on possessing firearms and ammunition after any misdemeanor crime of domestic violence, and South Carolina adds its own prohibition."),
   ],
   related=["bond-hearings", "expungements", "arrest-warrants"])

sp("bond-hearings",
   title="Bond Hearings in Dorchester, Berkeley & Charleston County | Summerville Defense Attorney",
   description="What happens at a South Carolina bond hearing, how bond amounts and conditions are set, how to get a bond reduced or modified, and why having a lawyer at the first hearing matters. Former officer Jack Frost.",
   h1="Bond Hearings in Summerville, Dorchester and Berkeley County", nav_label="Bond hearings",
   lead="The bond hearing is the first decision in a case, and it is made within a day of arrest. Here is what happens and how to make it go better.",
   summary="How bond is set, getting out, and changing conditions later.",
   body=(
       '<h2>When and where</h2>'
       f'<p>After a warrant arrest, South Carolina requires a bond hearing within 24 hours ({cite("bond", "S.C. Code § 22-5-510")}). In Dorchester County the hearing is held by a magistrate at the Dorchester County Detention Center on Hodge Road in Summerville; in Berkeley County at the Hill-Finklea Detention Center in Moncks Corner; in Charleston County at the Sheriff Al Cannon Detention Center in North Charleston. Municipal charges are heard by the municipal judge. For the most serious offenses—those punishable by life or death—only a circuit judge can set bond, which takes longer.</p>'
       '<h2>What the judge decides</h2>'
       + checks(["Whether to release on a personal recognizance (PR) bond—a promise to appear, with no money",
                 "The amount of a surety or cash bond, based on the charge, the person's ties to the community, criminal history and risk of flight or danger",
                 "Conditions: no contact with the alleged victim, no return to a residence, electronic monitoring, no alcohol, surrender of firearms"]) +
       '<p>The judge hears from the officer, the alleged victim if one appears, and the defendant or counsel. Most people say too much. A lawyer speaks to the factors that matter—job, family, residence, no history—and says nothing about the facts of the case.</p>'
       '<h2>After the hearing</h2>'
       + steps([("Posting bond.", " Cash to the clerk, or a bondsman for a percentage fee. Property bonds are possible but slow."),
                ("Reduction or modification.", " If bond is set too high or the conditions are unworkable—a no-contact order that keeps a parent from a child, a curfew that conflicts with work—a motion to reconsider goes to the court that set it, or to circuit court for General Sessions charges."),
                ("Stay compliant.", " A violated condition or a missed court date leads to revocation and a bench warrant. We calendar every date for you.")]) +
       '<h2>If someone you love was arrested</h2>'
       f'<p>Call {TEL}. Tell us the name, the charge and where they are being held. We can often appear at the hearing, and in every case we can prepare you for what the judge will ask and arrange the release once bond is set.</p>'
       + band("Someone in custody?", "Bond hearings happen fast. Call now and we will tell you what to expect in the next 24 hours.")
   ),
   faqs=[
       ("How much is bond in South Carolina?", "There is no schedule; the judge sets it case by case. Many misdemeanors get a PR bond; felonies vary widely."),
       ("Do I get bond money back?", "A cash bond is returned at the end of the case (less any fines) if every court date was kept. A bondsman's fee is not refundable."),
       ("Can bond conditions be changed?", "Yes, by motion to the court that set them. No-contact orders in domestic cases are the most common request."),
   ],
   related=["arrest-warrants", "domestic-violence-defense", "drug-charges"])

sp("expungements",
   title="Expungement in South Carolina | Who Qualifies, Waiting Periods & Cost | Summerville Attorney",
   description="South Carolina expungement explained: dismissed charges, first-offense convictions after three years, domestic violence after five, drug possession, Youthful Offender Act and PTI cases, the $250 solicitor fee, and which offenses can never be cleared. Summerville expungement attorney.",
   h1="Expungement in South Carolina: Who Qualifies, What It Costs and How Long It Takes", nav_label="Expungements",
   lead="A charge that was dismissed, a first offense from years ago, a mistake at nineteen. South Carolina lets many of them be erased. Here is who qualifies.",
   summary="Who qualifies, waiting periods, the fees, the circuit solicitors and the process.",
   body=(
       answer("Dismissed and not-guilty charges can be expunged at no cost as soon as the case is closed. Many first-offense convictions can be expunged after a waiting period: three years for a misdemeanor with a maximum penalty of 30 days or $1,000, five years for first-offense third-degree domestic violence, three years after completing the sentence for a first-offense simple possession conviction, and five years after completing a Youthful Offender Act sentence, provided there have been no other convictions. Conviction expungements cost $250 to the solicitor, $35 to the clerk of court and $25 to SLED. DUI, driving under suspension and other motor-vehicle offenses can never be expunged.", "The short answer")
       + '<h2>What can be expunged in South Carolina</h2>'
       + table(["Situation", "Eligibility", "Waiting period"], [
           ["Charge dismissed, nol prossed or not guilty (§ 17-1-40)", "Eligible; no fee", "None; apply once the case is closed"],
           ["Pretrial intervention completed (§ 17-22-150)", "Eligible", "On completion"],
           ["Conditional discharge for first-offense simple possession (§ 44-53-450)", "Eligible", "On completion"],
           ["First-offense misdemeanor with a maximum penalty of 30 days or $1,000 (§ 22-5-910)", "Eligible if no other convictions in the waiting period, in or out of state", "3 years"],
           ["First-offense third-degree domestic violence (§ 22-5-910)", "Eligible if no other convictions", "5 years"],
           ["First-offense simple possession or possession with intent to distribute (§ 22-5-930)", "Eligible if no other convictions", "3 years after completing the sentence, including probation"],
           ["Youthful Offender Act sentence (§ 22-5-920)", "Eligible for most nonviolent offenses; one per lifetime", "5 years after completing the sentence, no other convictions"],
           ["First-offense fraudulent check (§ 34-11-90)", "Eligible", "1 year"],
           ["DUI, DUAC, driving under suspension, other motor-vehicle offenses, violent crimes, offenses requiring sex-offender registration", "Not eligible", "Never"],
       ]) +
       f'<p>The 2018 reforms ({cite("expungement", "Act 254 of 2018; S.C. Code § 17-22-910 et seq.")}) expanded eligibility: multiple charges resolved at the same sentencing hearing are treated as one conviction when they are closely connected, first-offense drug possession became expungeable, and the Youthful Offender Act rules were broadened and made retroactive. Eligibility is judged on the offense you were actually convicted of, not the one you were charged with, which is why a plea to a lesser charge years ago can matter now.</p>'
       '<h2>What it costs</h2>'
       '<p>For a conviction expungement the statute sets three fees: $250 to the solicitor\'s office, which is nonrefundable even if the application is denied, $35 to the clerk of court and $25 to SLED. Expungement of a dismissed or not-guilty charge is free. Attorney\'s fees are a flat amount we quote up front, and we tell you before you pay anything whether you qualify.</p>'
       '<h2>The process</h2>'
       + steps([("Pull the record.", " We obtain your SLED criminal history and the court dispositions to confirm what is on the record and which entries qualify. People are often surprised by what is there, including arrests they thought were dismissed."),
                ("Apply to the right solicitor.", " Expungements are administered by the solicitor of the circuit where the charge was heard. Dorchester County is in the First Judicial Circuit, with the solicitor's office in St. George; Berkeley and Charleston counties are in the Ninth Judicial Circuit, with the office in North Charleston. A Summerville arrest can fall in either, depending on which county the stop was in."),
                ("Review and verification.", " The solicitor confirms eligibility, SLED verifies the record, and a circuit judge signs the order. For non-conviction expungements the clerk of court or summary court handles the order."),
                ("Destruction.", " The order directs the court, the arresting agency and SLED to destroy their records. Background checks run afterward come back clean for that charge, and you may lawfully say you were not arrested or convicted, with narrow exceptions for certain law-enforcement and licensing applications.")]) +
       '<p>Most applications take two to five months from filing to order, longer when the record has to be corrected first. The process is paper-driven and unforgiving: an incomplete application goes to the bottom of the pile.</p>'
       '<h2>Why it matters</h2>'
       '<p>Employers, landlords, licensing boards, schools and the military all run background checks. A dismissed charge from years ago still shows as an arrest until it is expunged, and a first-offense conviction that could have been cleared years ago keeps costing opportunities. The application is a small effort for a permanent result. If you are facing a new charge, the same analysis runs in reverse: we negotiate toward resolutions that preserve expungement eligibility, because a plea taken without that in mind can close the door for good.</p>'
       + band("Want to know if you qualify?", "Tell us the charge, the county and the year. We will check the statute and tell you honestly.")
   ),
   faqs=[
       ("How much does an expungement cost in South Carolina?", "Expungement of a dismissed charge is free. For a conviction, the fees are $250 to the solicitor, $35 to the clerk of court and $25 to SLED, plus a flat attorney's fee we quote up front."),
       ("How long after a conviction can I get an expungement in SC?", "Three years for most first-offense low-level misdemeanors, five years for first-offense third-degree domestic violence and Youthful Offender Act sentences, and three years after completing the sentence for first-offense drug possession, with no other convictions in that period."),
       ("Can a DUI be expunged in South Carolina?", "No. DUI, DUAC, driving under suspension and other offenses involving the operation of a motor vehicle are excluded from expungement."),
       ("Do I have to go to court for an expungement?", "Usually not. The application is processed on paper and signed by a judge."),
       ("Will an expunged charge show on a background check?", "No. The records are destroyed and you may lawfully answer that you were not arrested or convicted, with narrow exceptions for certain law-enforcement and licensing applications."),
       ("Which solicitor handles expungements for Summerville?", "Dorchester County arrests go through the First Circuit Solicitor in St. George; Berkeley and Charleston County arrests go through the Ninth Circuit Solicitor in North Charleston."),
   ],
   related=["drug-charges", "domestic-violence-defense", "traffic-tickets"])

sp("traffic-tickets",
   title="Driving Under Suspension & Traffic Tickets in South Carolina | Points, Penalties & Court | Summerville Attorney",
   description="South Carolina driving under suspension penalties under § 56-1-460, how points and suspensions work, why paying a ticket is a guilty plea, and what happens in Summerville Municipal Court and the Dorchester and Berkeley County magistrate courts.",
   h1="Traffic Tickets and Driving Under Suspension in South Carolina", nav_label="Traffic tickets",
   lead="Paying a ticket is pleading guilty. Before you do, know what it does to your license, your insurance and, for some charges, your criminal record.",
   summary="Points, suspensions, driving under suspension penalties, CDL holders and why not to just pay it.",
   body=(
       answer("Driving under suspension in South Carolina (S.C. Code § 56-1-460) is a criminal misdemeanor, not a ticket you can pay and forget. A first offense carries a $300 fine or up to 30 days in jail, or both; a second $600 or up to 60 days; a third $1,000 and up to 90 days, with harsher minimums when the suspension came from a DUI. The DMV also extends the original suspension. Ordinary moving violations add points to your record, twelve points brings a suspension, and paying the ticket is a guilty plea that posts the points. Many tickets can be reduced or resolved in a way that keeps points off your record.", "The short answer")
       + '<h2>Driving under suspension: penalties under § 56-1-460</h2>'
       + table(["Offense", "Suspension for any other reason", "Suspension for DUI, DUAC or a refusal"], [
           ["First", "$300 fine or up to 30 days in jail, or both", "$300 fine or 10 to 30 days in jail"],
           ["Second", "$600 fine or up to 60 days, or both", "$600 fine or 60 days to 6 months"],
           ["Third or later", "$1,000 fine and up to 90 days in jail or home detention", "$1,000 fine and 6 months to 3 years"],
       ]) +
       f'<p>Those are the figures in {ext("https://www.scstatehouse.gov/code/t56c001.php", "S.C. Code § 56-1-460")}. On top of the sentence, the DMV extends the suspension for a further period when it receives the conviction, so each offense pushes the day you can drive legally further away. The most common reason people are driving suspended is one they did not know about: a ticket that went unpaid, a missed court date, a lapse in insurance or an unpaid reinstatement fee. The first thing we do is pull your DMV record to find out why you were suspended and what it takes to fix it, because a driver who is reinstated before the court date is in a far better position than one who is not.</p>'
       '<h2>Points and suspensions</h2>'
       f'<p>South Carolina assigns points to moving violations ({cite("points", "S.C. Code § 56-1-720")}): two for speeding 10 mph or less over the limit, four for 11 to 24 over, six for 25 or more over or for reckless driving, four for disobeying a traffic signal or following too closely, and so on. Twelve or more points brings a suspension, and points are halved after a year. Insurance companies read the same record and price it, and a six-point ticket can cost more in premiums over three years than the fine.</p>'
       '<h2>Tickets that are more than tickets</h2>'
       + checks(["<b>Reckless driving</b> is a criminal misdemeanor with six points; a second conviction within five years brings a three-month suspension.",
                 "<b>Driving under suspension</b> is a criminal charge with jail exposure that grows with each offense, and it is never expungeable.",
                 "<b>Leaving the scene, racing and habitual-offender status</b> each carry consequences far beyond a fine, including multi-year license revocations.",
                 "<b>Failure to appear or pay.</b> Missing a court date lets the court convict you in your absence and suspends your license until the fine is paid and the reinstatement fee cleared.",
                 "<b>Commercial drivers.</b> A ticket in a personal vehicle can still put a CDL at risk, and masking is prohibited; never pay one without checking.",
                 "<b>Out-of-state drivers.</b> South Carolina reports convictions to your home state under the Driver License Compact, where the points may count differently."]) +
       '<h2>What we can often do</h2>'
       '<p>Negotiate a reduction to a non-moving or lower-point violation, arrange a defensive-driving resolution where the court allows it, challenge the speed measurement and the legality of the stop when the facts support it, get a suspension cleared before the court date so a driving-under-suspension charge can be dismissed or reduced, and appear for you so you do not lose a workday in court. For serious charges, we prepare for trial.</p>'
       '<h2>Which court</h2>'
       '<p>Tickets are heard in the municipal court of the town where you were stopped, such as Summerville Municipal Court at Town Hall on South Main Street, Goose Creek or North Charleston, or in the county magistrate\'s court for stops by the sheriff or the Highway Patrol, which for Dorchester County means the Summerville magistrate at 212 Deming Way or the St. George office. Your ticket shows the court and the date. If you miss the date, the court can convict you in your absence and suspend your license for failure to pay.</p>'
       + band("Got a ticket, or charged with driving under suspension?", "Send us a photo of it. We will tell you the points, the risk, and whether it is worth fighting.")
   ),
   faqs=[
       ("What is the penalty for driving under suspension in South Carolina?", "A first offense is a $300 fine or up to 30 days in jail, or both; a second is $600 or up to 60 days; a third is $1,000 and up to 90 days. If the suspension was for DUI the minimums are higher, up to six months to three years for a third offense. The DMV also extends the suspension."),
       ("Can I just pay a speeding ticket in South Carolina?", "Yes, but paying is a guilty plea and the points post to your record. For anything above a minor speed, ask first."),
       ("Can driving under suspension be expunged in SC?", "No. Offenses involving the operation of a motor vehicle are excluded from South Carolina's expungement statute."),
       ("Do I have to appear in court for a traffic ticket?", "For most tickets an attorney can appear for you. Some charges, including driving under suspension, require your presence."),
       ("Will a ticket in South Carolina affect my Georgia or North Carolina license?", "Usually yes; states share convictions through the Driver License Compact."),
   ],
   related=["dui-lawyer-summerville-sc", "expungements", "arrest-warrants"])

sp("arrest-warrants",
   title="Bench Warrants & Arrest Warrants in South Carolina | How to Check & Surrender | Summerville Attorney",
   description="How to find out whether there is a bench warrant or arrest warrant for you in South Carolina, what a missed court date triggers under § 22-5-115, how to lift a bench warrant, and how to surrender with a bond hearing arranged in Dorchester, Berkeley or Charleston County.",
   h1="Bench Warrants and Arrest Warrants in South Carolina: How to Check and What to Do", nav_label="Arrest warrants",
   lead="A warrant does not go away, and being picked up at work or at a traffic stop is the worst way to deal with it. There is a better one.",
   summary="Confirming a warrant, lifting a bench warrant, and surrendering with counsel.",
   body=(
       answer("A bench warrant is issued by a judge when you miss a court date or violate a court order; an arrest warrant is issued on an officer's sworn affidavit of probable cause. Both stay active until they are served or recalled, and a bench warrant on a traffic case also suspends your license. You can check for warrants through the county's public case index or by having a lawyer call the court, which does not expose you the way calling the sheriff yourself can. The fix for a bench warrant is a motion to recall it and reset the case; the fix for an arrest warrant is a planned surrender with the bond hearing arranged so you are processed and released the same day.", "The short answer")
       + '<h2>Two kinds of warrants</h2>'
       + checks([f"<b>Arrest warrants</b> are issued by a magistrate or municipal judge on an officer's sworn affidavit that there is probable cause you committed a crime ({cite('warrants', 'S.C. Code § 22-5-110')}). Jack has written hundreds; he knows what a sufficient affidavit looks like and what a deficient one looks like, and the affidavit is the first thing we attack.",
                 f"<b>Bench warrants</b> are issued by the judge when you fail to appear for a court date or violate a bond condition or other order ({ext('https://www.scstatehouse.gov/code/t22c005.php', 'S.C. Code § 22-5-115')}). In magistrate and municipal court the judge may instead try you in your absence, convict you and suspend your license for failing to pay. About ninety days after a bench warrant issues, the court moves the case to failure-to-appear status, where it waits indefinitely for you to be stopped."]) +
       '<h2>How to find out whether there is a warrant</h2>'
       + steps([("Search the public index.", " Dorchester, Berkeley and Charleston counties post pending cases and court dates on the South Carolina Judicial Branch's public index. A case with a missed date and a bench warrant usually shows a disposition code that tells the story."),
                ("Do not call the sheriff yourself.", " The sheriff's office and the magistrate's court can confirm active warrants, but a call that gives your name and location can prompt a visit. If an officer or investigator asks you to “come in and talk,” there is a reasonable chance a warrant already exists."),
                ("Let us check.", " We confirm whether a warrant exists and what it charges through the issuing court or agency without exposing you, and we find out whether the case has gone to failure-to-appear status or been tried in your absence.")]) +
       '<h2>Lifting a bench warrant</h2>'
       '<p>If you missed a court date, the remedy is a motion to recall the bench warrant and reset the case, which is faster and cheaper than being arrested on it. Many people miss dates because the notice went to an old address or the date was moved; courts in Dorchester and Berkeley counties are generally willing to reset once when counsel appears with you and explains. If the court already tried you in your absence, we move to reopen the case. If the DMV suspended your license for the failure to appear, clearing the case is also the first step to reinstating it, and until then you should not drive.</p>'
       '<h2>Surrendering on an arrest warrant</h2>'
       + steps([("Do not wait for the knock.", " Warrants are served at traffic stops, at work and at 6 a.m. at home. None of those lets you prepare."),
                ("Arrange the surrender.", " We schedule a time to turn yourself in at the detention center with the bond hearing arranged. In Dorchester County, bond court sits at the Summerville magistrate's office at 9 a.m. and 3 p.m. every day, including weekends and holidays, and arrests are booked at the Dorchester County Detention Center on Hodge Road in Summerville; Berkeley County uses the Hill-Finklea Detention Center in Moncks Corner and Charleston County the Al Cannon Detention Center in North Charleston. For some charges we can ask that a courtesy summons be used instead of an arrest."),
                ("Prepare for bond.", " Employment letter, residence proof, family present. That is what the judge weighs. See " + A("bond-hearings", "bond hearings") + "."),
                ("Start the defense.", " A warrant is the beginning of a case, not a verdict.")]) +
       '<h2>Warrants from other counties or states</h2>'
       '<p>Charleston County warrants are served in Dorchester County and vice versa, and out-of-state warrants lead to extradition holds that can keep you in jail for weeks while the other state decides whether to come get you. We coordinate with the issuing jurisdiction so a surrender happens once, in the right place.</p>'
       + callout("<b>Frost first:</b> if an officer or investigator calls and asks you to “come in and talk,” call us before you go.")
       + band("Think there is a warrant with your name on it?", "Call. We will find out quietly and arrange the surrender on your terms.")
   ),
   faqs=[
       ("How do I check for a bench warrant in South Carolina?", "Search the county's public case index for your name and look for a missed court date, or have a lawyer call the court. Calling the sheriff's office yourself can prompt an arrest."),
       ("What happens if I miss a court date in South Carolina?", "In magistrate or municipal court the judge can issue a bench warrant or try you in your absence; on a traffic charge the DMV suspends your license for the failure to appear. After about ninety days the case goes to failure-to-appear status and the warrant waits for you."),
       ("How do I get a bench warrant lifted?", "Your lawyer files a motion to recall the warrant and reset the case, and appears with you. Courts usually grant one reset when the reason is explained."),
       ("Will I have to spend the night in jail if I turn myself in?", "Usually not when a surrender is arranged with a bond hearing scheduled. Dorchester County holds bond court twice a day, so processing and release often happen the same day."),
   ],
   related=["bond-hearings", "drug-charges", "domestic-violence-defense"])
