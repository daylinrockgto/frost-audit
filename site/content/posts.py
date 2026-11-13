"""Blog posts: local news and community questions, answered by the attorney who owns the topic.

Authorship rule: Tara writes probate and estate planning; Jack writes criminal defense. Each post
names the other attorney as reviewer. Outbound links go to the original reporting or official
sources (news outlets, county and state sites) and to the community threads where the question is
being asked (Nextdoor, Reddit — nofollow). Verified URLs come from local_data.json via local.link().
"""
from .base import page, A, ext, img, p, ul, checks, steps, callout, answer, band, esc, table
from . import firm
from .local import cite, link, LINKS

TEL = f'<a href="tel:{firm.PHONE_E164}">{firm.PHONE}</a>'
DATE = "2026-09-16"


def src(*keys):
    """Build a sources list from verified link keys (skips unknown keys)."""
    out = []
    for k in keys:
        l = LINKS.get(k)
        if l:
            out.append((l["label"], l["url"], l.get("nofollow", False)))
    return out


def post(slug, **kw):
    kw.setdefault("kind", "post")
    kw.setdefault("hub", "blog")
    kw.setdefault("date", DATE)
    kw.setdefault("cta", False)
    kw.setdefault("changefreq", "yearly")
    kw.setdefault("priority", 0.5)
    return page("blog/" + slug, **kw)


# ----------------------------------------------------------------------------- 1. New residents
post("new-summerville-residents-estate-plan", hero_image="cover-new-residents.jpg", hero_caption="New construction in Summerville", author="tara", reviewer="jack", category="Estate planning",
     title="Moved to Summerville? Five Documents South Carolina Wants Redone",
     description="Dorchester and Berkeley counties keep adding new residents. If your will and powers of attorney were signed in another state, here is what still works in South Carolina and what does not.",
     h1="Moved to Summerville? Five documents South Carolina wants you to redo",
     summary="Thousands of families arrive in Nexton, Cane Bay and Carnes Crossroads every year with estate documents from somewhere else. Most of the wills still work. Most of the powers of attorney do not.",
     lead="Every week the local papers report another subdivision approved in Dorchester or Berkeley County. If you are one of the families moving in, your estate plan probably moved with you—and part of it stopped working at the state line.",
     body=(
         '<h2>What the growth stories leave out</h2>'
         f'<p>Read {link("pc_summerville", "the Post and Courier’s Summerville coverage")} or the {link("berkeley_independent", "Berkeley Independent")} for a month and you will see the pattern: new neighborhoods off Nexton Parkway, Cane Bay Boulevard and Highway 17-A, new schools, new traffic counts. What the stories never mention is that the newcomers\' legal paperwork was written for Ohio, New York or Georgia. That matters more than most people expect.</p>'
         '<h2>The five documents, in order of urgency</h2>'
         + steps([
             ("Your durable power of attorney.", f" South Carolina adopted the Uniform Power of Attorney Act in 2017 ({cite('poa_act', 'S.C. Code Title 62, Article 8')}). A power of attorney signed elsewhere is generally recognized, but South Carolina requires a durable POA to be recorded with the county register of deeds before an agent can act during incapacity, and local banks are quick to reject unfamiliar forms. A new South Carolina POA in recordable form solves both problems."),
             ("Your health care power of attorney and living will.", f" Hospitals here look for South Carolina's own statutory forms ({cite('hcpoa', '§§ 62-5-503 and 62-5-504')} and the {cite('living_will_act', 'Death with Dignity Act')}). An out-of-state directive may be honored, but in an emergency room nobody wants to be the test case. These are quick to redo."),
             ("Your will.", f" A will valid where you signed it is valid here. The problems are practical: your named personal representative may now live 800 miles away, your guardian nomination may be stale, and the will may not be self-proved in a way the Dorchester or Berkeley County probate court accepts without a witness affidavit ({cite('self_proved', '§ 62-2-503')}). We usually re-sign a South Carolina will rather than patch the old one."),
             ("Your trust, if you have one.", " The trust itself travels fine. The funding does not: your new Lowcountry home was deeded to you personally at closing, not to the trust, unless someone caught it. Retitling the house is a one-page deed—but only if someone does it."),
             ("Your beneficiary designations.", " New job, new 401(k), new life insurance through the new employer. Each one has a beneficiary form that overrides your will. Check them the same week you change your driver's license."),
         ]) +
         '<h2>The county question</h2>'
         f'<p>Summerville sits in Dorchester County—except when it doesn\'t. Nexton, Cane Bay, Carnes Crossroads and much of the growth north of I-26 carry a Summerville address in <em>Berkeley</em> County. Your county decides where your estate will be probated, where a guardianship is filed and which sheriff serves a warrant. Our {A("probate-courts", "guide to the three probate courts")} and the {A("service-areas/nexton", "Nexton")} and {A("service-areas/cane-bay", "Cane Bay")} pages explain which is which.</p>'
         '<h2>What people are asking their neighbors</h2>'
         f'<p>The question shows up on {link("nextdoor_summerville", "Nextdoor for Summerville")} and in {link("reddit_charleston", "r/Charleston")} threads every few weeks: “Do I need a new will now that I\'m in South Carolina?” The honest answer is <em>probably not the will, definitely the powers of attorney, and check the deed.</em> A plan review is a flat fee and takes one meeting; see {A("estate-plan-review", "estate plan reviews")}.</p>'
         + callout("<b>Frost first:</b> before you sign the “South Carolina update” a moving-related service emails you, let us read it. We see plans every month that were “updated” without the recording language, the witnesses, or the deed.")
     ),
     sources=src("pc_summerville", "berkeley_independent", "nextdoor_summerville", "reddit_charleston") + [("S.C. Code Title 62, Article 8 (Uniform Power of Attorney Act)", "https://www.scstatehouse.gov/code/t62c008.php", False)],
     related=["estate-plan-review", "power-of-attorney", "probate-courts"],
     faqs=[("Is my out-of-state will valid in South Carolina?", "Yes, if it was valid where it was signed. We still recommend re-signing a South Carolina will so it is self-proved here and names people who can actually serve."),
           ("Do I have to record my power of attorney in South Carolina?", "A durable power of attorney must be recorded with the register of deeds in your county before your agent can act once you are incapacitated. We prepare it in recordable form and record it when needed.")])

# ----------------------------------------------------------------------------- 2. Hurricane season
post("hurricane-season-documents-dorchester-county", hero_image="cover-hurricane.jpg", hero_caption="The go-bag, documents included", author="tara", reviewer="jack", category="Estate planning",
     title="Hurricane Season: Four Documents for the Go-Bag | Dorchester County",
     description="Every evacuation order raises the same question in Dorchester and Berkeley County homes: where is the will? Four documents to secure now, and what South Carolina law does if an original will is lost.",
     h1="Before the next evacuation order: four documents Dorchester County families should have in the go-bag",
     summary="When the county issues an evacuation order, the will is the last thing anyone thinks about—and the one document South Carolina law treats harshly if it goes missing.",
     lead="Hurricane season runs through November, and the Lowcountry's news outlets spend it tracking cones and evacuation zones. Here is the legal checklist that never makes the broadcast.",
     body=(
         '<h2>Why a lost will is worse than a lost roof</h2>'
         '<p>If an original will cannot be found after death, South Carolina presumes the person destroyed it on purpose. A copy can sometimes be admitted, but only after a court proceeding with evidence that the will was not revoked—expensive, slow, and easy for an unhappy relative to contest. A storm-soaked filing cabinet in a flooded garage produces exactly that situation.</p>'
         '<h2>The four documents</h2>'
         + steps([
             ("The original will (and trust).", " Keep it in a sealed, waterproof pouch with the go-bag, or leave the original with your attorney and keep a copy at home with a note saying where the original is. Our office holds originals for clients who ask."),
             ("Powers of attorney.", " If you are evacuated and a spouse or parent is hospitalized somewhere else, the health care power of attorney is what lets you speak for them by phone. Keep signed copies in the bag and photos on your phone."),
             ("Insurance policies and a home inventory.", " Not estate documents, but the same pouch: policy numbers, agent contacts, and a phone video walking through every room. Claims move faster with proof."),
             ("Deeds, titles and account list.", " A one-page list of accounts, policies and where the deeds are recorded. If the worst happens during a storm, this is what your personal representative will need first."),
         ]) +
         '<h2>Where to get the official information</h2>'
         f'<p>Evacuation zones and orders come from {link("scemd", "the South Carolina Emergency Management Division")} and {link("dorchester_emd", "Dorchester County Emergency Management")}; the local outlets—{link("live5", "Live 5 News")}, {link("abcnews4", "ABC News 4")} and {link("wcbd", "WCBD News 2")}—carry the county announcements and the traffic reversals on I-26. Bookmark them now, before the cone appears.</p>'
         '<h2>A note for families with older parents</h2>'
         f'<p>Evacuations are when families discover that nobody has authority to move a parent, talk to the facility, or pay the bill from the hotel in Columbia. If your parent does not have a durable power of attorney and a health care power of attorney, and still has the capacity to sign them, do it before the season peaks. If they no longer can, read our page on {A("guardianship-and-conservatorship", "guardianship and conservatorship")}.</p>'
         + callout("<b>Frost first:</b> the week after a storm, contractors and “document services” go door to door. A deed transfer signed under stress is the kind of thing we spend the next year undoing. Call before you sign.")
     ),
     sources=src("scemd", "dorchester_emd", "live5", "abcnews4", "wcbd", "nextdoor_summerville"),
     related=["last-will-and-testament", "power-of-attorney", "probate-process"],
     faqs=[("Can a copy of a will be probated in South Carolina?", "Sometimes, through a formal proceeding with evidence that the original was not revoked. It is far easier to keep the original safe—or leave it with your attorney."),
           ("Should I keep my will in a bank safe-deposit box?", "It is safe from water, but the box may be sealed at death until the personal representative is appointed—and the appointment needs the will. If you use a box, make sure a co-owner can open it.")])

# ----------------------------------------------------------------------------- 3. Guardianship for an aging parent
post("guardianship-aging-parent-summerville", hero_image="cover-guardianship.jpg", hero_caption="Planning for an aging parent", author="tara", reviewer="jack", category="Probate",
     title="Guardianship for an Aging Parent in Summerville | Nextdoor Question Answered",
     description="“Who handles guardianship for my mom in Summerville?” A former Dorchester County Associate Probate Judge explains the process, the alternatives, and when a power of attorney can still avoid it.",
     h1="“Who handles guardianship for my aging parent in Summerville?” The Nextdoor question, answered",
     summary="It is one of the most common legal questions on Summerville's neighborhood forums, and the answers usually miss the first step: whether a guardianship is needed at all.",
     lead="A neighbor posts that Mom has stopped paying bills and will not see a doctor, and asks who to call. Thirty replies later, nobody has mentioned the probate court. Here is what actually happens.",
     body=(
         answer("Guardianship and conservatorship for an adult in Summerville are filed in the probate court of the county where the person lives—Dorchester County for most Summerville addresses, Berkeley County for Nexton, Cane Bay and Carnes Crossroads. Frost Law Group handles these cases; Tara Frost served as an Associate Probate Judge in Dorchester County, where they are heard. Before filing, we check whether a power of attorney can still be signed, because it is faster, cheaper and private.", "The short answer")
         + '<h2>First question: can Mom still sign?</h2>'
         '<p>Capacity to sign a power of attorney is a lower bar than people assume. A parent with early dementia who understands, on a good morning, that she is naming her daughter to handle her money and her medical decisions can usually sign valid documents. If that is your situation, the whole guardianship question may disappear with two signatures and a notary. We meet clients at home or at a facility for exactly this reason.</p>'
         '<h2>If she cannot: what a guardianship involves</h2>'
         + steps([
             ("A petition in probate court.", f" Filed under South Carolina's adult protective proceedings statutes ({cite('guardianship', 'S.C. Code Title 62, Article 5')}) with a physician's report on the person's condition."),
             ("Examiners and a guardian ad litem.", " The court appoints professionals to evaluate the person and report; the guardian ad litem represents the person's interests."),
             ("Notice to the family.", " Spouse, children and other close relatives receive notice and can object or ask to serve."),
             ("A hearing.", " The judge decides whether the person is incapacitated and, if so, who should serve and with what powers—often a limited guardianship tailored to the actual need."),
             ("Ongoing reporting.", " Guardians file annual reports; conservators file inventories and accountings and usually post a bond."),
         ]) +
         '<h2>What it costs and how long it takes</h2>'
         '<p>Filing fees, examiner fees and attorney\'s fees together commonly run into the low thousands of dollars for an uncontested case, and two to four months from filing to hearing depending on the court\'s docket. Contested cases—two siblings who each want to serve, or a parent who objects—take longer and cost more. Emergency appointments are available when someone is in immediate danger.</p>'
         '<h2>Where the neighbors\' advice goes wrong</h2>'
         + checks(["“Just get power of attorney” — a POA cannot be signed <em>for</em> someone who lacks capacity; that is what guardianship is for.",
                   "“Add yourself to her bank account” — that makes you a joint owner, exposes the money to your creditors, and changes who inherits it.",
                   "“The doctor can declare her incompetent” — a doctor's opinion is evidence; only the probate court can appoint a guardian.",
                   "“Adult Protective Services will handle it” — APS investigates abuse and neglect; it does not manage a parent's finances for the family."]) +
         f'<p>You will find versions of all four on {link("nextdoor_summerville", "Nextdoor")} and in {link("reddit_charleston", "r/Charleston")} threads. For non-legal help—home care, respite, Medicaid waiver programs—{link("trident_aging", "the Trident Area Agency on Aging")} is the right first call.</p>'
         + band("Worried about a parent?", "Call and describe what is happening. We will tell you whether documents can still be signed or a petition is needed, and what each path costs.")
     ),
     sources=src("nextdoor_summerville", "reddit_charleston", "trident_aging", "dorchester_probate_site") + [("S.C. Code Title 62, Article 5 (protection of persons under disability)", "https://www.scstatehouse.gov/code/t62c005.php", False)],
     related=["guardianship-and-conservatorship", "power-of-attorney", "probate-courts"],
     faqs=[("Can I get guardianship of my mother without a lawyer?", "The probate court accepts pro se petitions, but the medical evidence, notice requirements and hearing are unforgiving of mistakes. Most families use an attorney for at least the petition and hearing."),
           ("Which court handles guardianship for a Summerville address?", "Dorchester County Probate Court for most of Summerville; Berkeley County Probate Court for Nexton, Cane Bay, Carnes Crossroads and other Summerville addresses north of the county line.")])

# ----------------------------------------------------------------------------- 4. Expungement clinics
post("expungement-clinics-who-qualifies-dorchester-berkeley", hero_image="cover-expungement.jpg", hero_caption="Waiting at the county office", author="jack", reviewer="tara", category="Criminal defense",
     title="Expungement Clinics in the News: Who Qualifies in Dorchester & Berkeley",
     description="Solicitors and legal aid groups hold expungement clinics around the Lowcountry. Before you stand in line, a former officer explains who qualifies under South Carolina's 2018 reforms and what the clinic can and cannot do.",
     h1="Saw the expungement clinic in the news? Here is who qualifies in Dorchester and Berkeley County",
     summary="Every few months a Lowcountry outlet covers a free expungement clinic. The lines are long and about half the people in them do not qualify—yet. Here is how to know before you go.",
     lead="Expungement clinics are a genuinely good thing. They are also confusing, because eligibility depends on the exact charge, the exact disposition and the calendar. Check these five things first.",
     body=(
         '<h2>What a clinic can do</h2>'
         '<p>A clinic helps you pull your record, confirm eligibility and complete the application that goes to the solicitor\'s office—the First Circuit for Dorchester and Berkeley counties, the Ninth Circuit for Charleston. The volunteers are usually law students and legal-aid attorneys. What they cannot do is change the law: if your charge is not eligible, or the waiting period has not run, the answer is the same at the clinic as anywhere else.</p>'
         '<h2>The five questions that decide eligibility</h2>'
         + steps([
             ("Was the charge dismissed, nol prossed or found not guilty?", " Then it is eligible now, at no cost. Many people do not realize a dismissed charge still shows on a background check until it is expunged."),
             ("Was it a first-offense misdemeanor with a maximum penalty of 30 days or $1,000?", f" Eligible three years after the conviction if you have had no other convictions ({cite('expungement_misdemeanor', 'S.C. Code § 22-5-910')}). Third-degree domestic violence, first offense, waits five years."),
             ("Was it first-offense simple possession or paraphernalia?", f" Eligible if handled through a conditional discharge ({cite('conditional_discharge', '§ 44-53-450')}) and three years have passed since completion—one of the 2018 changes."),
             ("Were you sentenced under the Youthful Offender Act?", f" Many nonviolent YOA sentences are eligible five years after completion with no later convictions ({cite('yoa', '§ 22-5-920')})."),
             ("Is it a DUI, a traffic offense, or a violent crime?", " Not eligible. No clinic and no attorney can change that."),
         ]) +
         '<h2>What changed in 2018</h2>'
         f'<p>{cite("expungement", "Act 254 of 2018")} expanded expungement in three ways people still do not know about: multiple charges resolved on the same sentencing sheet can be treated as one offense; first-offense drug possession became eligible; and expungement now applies to convictions even if the person later moved on to a clean record in a different way. If you were told “no” before 2018, ask again.</p>'
         '<h2>Before you go</h2>'
         + checks(["Pull your own record: the clinic will, but knowing your exact charges and dispositions beforehand saves an hour in line.",
                   "Bring photo identification and the case numbers if you have them.",
                   "Count the years from the date of conviction (or completion of the program), not the date of arrest.",
                   "If any charge is pending anywhere, resolve it first; a pending charge blocks expungement."]) +
         f'<p>Clinic announcements run in {link("pc_summerville", "the Post and Courier")}, on {link("live5", "Live 5 News")} and on the counties\' own pages. If you would rather not wait for the next one, we file expungements year-round for a flat fee; see {A("expungements", "expungements")}.</p>'
         + callout("<b>Frost first:</b> if the charge you want cleared was one of several from the same night, ask about the same-sentencing-sheet rule before assuming only one can be expunged.")
     ),
     sources=src("pc_summerville", "live5", "sccourts_expungement") + [("S.C. Code Title 22, Chapter 5 (expungement of criminal records)", "https://www.scstatehouse.gov/code/t22c005.php", False), ("S.C. Code Title 17, Chapter 22 (expungement procedure)", "https://www.scstatehouse.gov/code/t17c022.php", False)],
     related=["expungements", "drug-charges", "domestic-violence-defense"],
     faqs=[("Are expungement clinics free?", "Usually the clinic's help is free; the statutory fees for conviction expungements still apply unless the sponsor covers them. Expunging a dismissed charge is free."),
           ("Can I expunge a charge from another county at a Dorchester County clinic?", "The application goes to the solicitor for the circuit where the charge was heard, so a Charleston County charge goes to the Ninth Circuit regardless of where you live now.")])

# ----------------------------------------------------------------------------- 5. School zones
post("school-zone-traffic-enforcement-summerville", hero_image="cover-school-zone.jpg", hero_caption="School morning in Summerville", author="jack", reviewer="tara", category="Criminal defense",
     title="School-Zone Enforcement in Summerville: What a Ticket Really Costs",
     description="Each August, Summerville police and the Dorchester County Sheriff's Office announce school-zone enforcement. A former officer explains points, insurance, the school-bus charge that is not a ticket, and when to fight.",
     h1="Back-to-school traffic enforcement in Summerville: what a ticket really costs",
     summary="The August press releases promise extra patrols around Dorchester District Two schools. The tickets that follow cost more than the fine on the front.",
     lead="Every year the same announcement runs the week school starts: extra patrols on Central Avenue, Old Trolley Road and Highway 78 around the schools. Here is what the tickets do after you pay them.",
     body=(
         '<h2>The fine is the small part</h2>'
         f'<p>South Carolina puts points on your license for moving violations ({cite("points", "S.C. Code § 56-1-720")}): two for speeding ten over or less, four for eleven to twenty-four over, six for twenty-five or more over. Points post when you pay the ticket, because paying is a guilty plea. Insurance carriers read the same record. A four-point ticket can cost several times its fine in premiums over three years, and twelve points brings a suspension.</p>'
         '<h2>The charge that is not a ticket</h2>'
         '<p>Passing a stopped school bus with its stop arm out is a criminal misdemeanor in South Carolina, not a simple traffic infraction—six points, a fine that can run into the thousands on a first offense, and a court date you should not handle alone. Bus cameras in Dorchester District Two mean these charges arrive by mail weeks after the fact. Call before you respond.</p>'
         '<h2>Who is writing the tickets</h2>'
         f'<p>Inside town limits it is the {link("summerville_pd", "Summerville Police Department")}, and the ticket goes to Summerville Municipal Court. Outside the limits it is the Dorchester County Sheriff\'s Office or the Highway Patrol, and the case goes to the county magistrate. The court on the ticket tells you which. {link("dd2", "Dorchester District Two")} publishes the school calendar, which is also the enforcement calendar.</p>'
         '<h2>When fighting it makes sense</h2>'
         + checks(["Any ticket of four points or more, if your record is otherwise clean—reductions to non-moving violations are common.",
                   "Anything involving a commercial driver's license, where a personal-vehicle ticket can cost the job.",
                   "Reckless driving, driving under suspension or a school-bus charge—criminal charges with jail exposure.",
                   "A ticket you believe is wrong: the speed measurement, the school-zone timing, the signage."]) +
         '<p>For a two-point ticket with no CDL and a clean record, paying it is often the rational choice. We will tell you that on the phone.</p>'
         + callout("<b>Frost first:</b> photograph the ticket and text it to us before the court date printed on it. Missing that date turns a fine into a bench warrant and a license suspension.")
     ),
     sources=src("summerville_pd", "dd2", "live5", "pc_summerville") + [("S.C. Code Title 56, Chapter 1 (driver's license points)", "https://www.scstatehouse.gov/code/t56c001.php", False)],
     related=["traffic-tickets", "arrest-warrants", "expungements"],
     faqs=[("Do school-zone speeding fines double in South Carolina?", "South Carolina does not automatically double fines in school zones the way some states do, but the points, the insurance impact and the officer's discretion on how the ticket is written are all worse. Treat it as a four- or six-point ticket, not a parking fine."),
           ("Can a traffic ticket be expunged?", "No. Traffic convictions are not eligible for expungement in South Carolina, which is why the decision to pay or fight matters.")])

# ----------------------------------------------------------------------------- 6. Reddit: do I need a probate lawyer
post("do-i-need-a-probate-lawyer-south-carolina-reddit", hero_image="cover-probate-lawyer.jpg", hero_caption="Probate court forms", author="tara", reviewer="jack", category="Probate",
     title="Reddit Asks: Do I Need a Probate Lawyer in SC? A Former Judge Answers",
     description="The question comes up constantly in r/Charleston and r/southcarolina. An honest answer from a former Dorchester County Associate Probate Judge: when you can do it yourself, when you should not, and how to tell.",
     h1="Reddit asks: “Do I really need a probate lawyer in South Carolina?” An honest answer from a former probate judge",
     summary="Half the replies say “just use the court forms,” the other half say “always hire a lawyer.” Both are right, for different estates. Here is how to tell which one you have.",
     lead="It is one of the most-asked legal questions in the Lowcountry's online forums, and the replies are usually somebody's one experience. Here is the view from the bench.",
     body=(
         answer("You can probate a simple South Carolina estate yourself: the probate court's forms are public, the clerks are helpful, and an estate with a clear will, cooperative heirs, no real estate to sell and no creditor problems is manageable. You should hire a lawyer when the estate owns real estate that must be sold or divided, when heirs disagree, when there is a business or out-of-state property, when a creditor claim is large, or when you are the personal representative and the beneficiaries are already unhappy. Call and we will tell you which yours is—for free, on the phone.", "The short answer")
         + '<h2>Estates you can usually handle alone</h2>'
         + checks([f"A small estate that qualifies for the affidavit—a probate estate of $45,000 or less after liens, collected by affidavit ({A('small-estate-affidavit', 'details')}).",
                   "A surviving spouse inheriting everything under a clear will, with all the accounts already joint or beneficiary-designated.",
                   "An informal estate where the only real asset is a house passing to one heir who is keeping it, and every heir signs waivers.",
                   f"Any of the above where the personal representative is organized and follows the eight-month creditor rule ({cite('creditor_period', '§ 62-3-801')}) instead of distributing early."]) +
         '<h2>Estates that go wrong without help</h2>'
         + checks(["Real estate that must be sold, especially heirs' property with several owners or an old family parcel with title problems.",
                   "A will that treats children unequally, was signed late in life, or was prepared by one child.",
                   "A business, rental property, or anything in another state.",
                   "Creditor claims larger than a few thousand dollars, or a Medicaid estate-recovery claim.",
                   "A beneficiary who is a minor, has a disability, or cannot be found.",
                   "Any estate where a beneficiary has already hired a lawyer."]) +
         '<h2>What the forum answers miss</h2>'
         f'<p>Two things. First, hiring a probate attorney is not all-or-nothing: we regularly handle just the opening and the inventory, or just the closing, for a flat fee, while the family does the rest. Second, attorney\'s fees for the estate are paid from the estate, not from the personal representative\'s pocket. That changes the math for a lot of the people asking in {link("reddit_charleston", "r/Charleston")} and {link("reddit_southcarolina", "r/southcarolina")}.</p>'
         '<h2>Where to start if you are doing it yourself</h2>'
         f'<p>The {link("sccourts_probate_forms", "South Carolina Judicial Branch publishes the probate forms")} used statewide, and each county court has a self-help page. Read our {A("probate-process", "step-by-step guide")} first, then the {A("executor-duties", "personal representative checklist")}. If you get stuck, a one-hour consultation is cheaper than unwinding a mistake.</p>'
         + band("Not sure which kind of estate you have?", "Tell us what was owned and who the heirs are. We will say honestly whether you need us.")
     ),
     sources=src("reddit_charleston", "reddit_southcarolina", "sccourts_probate_forms", "dorchester_probate_site"),
     related=["probate-process", "small-estate-affidavit", "executor-duties"],
     faqs=[("How much does a probate lawyer cost in South Carolina?", "There is no statutory percentage. Most firms, including ours, quote flat fees for uncontested estates and hourly rates with an estimate for contested matters. Fees are paid from the estate."),
           ("Can the personal representative hire a lawyer for the estate without the heirs' permission?", "Yes. Reasonable attorney's fees are an administration expense, though beneficiaries can object to unreasonable ones at the accounting.")])

# ----------------------------------------------------------------------------- 7. DV arrests in the news
post("domestic-violence-arrest-first-72-hours-dorchester-county", hero_image="cover-domestic-violence.jpg", hero_caption="The courthouse at dawn", author="jack", reviewer="tara", category="Criminal defense",
     title="After a Domestic Violence Arrest in Dorchester County: The First 72 Hours",
     description="Local police blotters report domestic violence arrests every week. What happens in the first three days—bond, no-contact orders, going home—and the mistakes that turn one charge into two. By a former officer.",
     h1="After a domestic violence arrest in Dorchester County: the first 72 hours",
     summary="The arrest makes the blotter; what happens next does not. A former officer walks through bond, the no-contact order, and the three mistakes that create a second charge.",
     lead="Scan the weekly arrest reports in the local papers and you will see “domestic violence, 3rd degree” more than almost any other charge. The first three days after that arrest decide more than most people realize.",
     body=(
         '<h2>Hour 0–24: the bond hearing</h2>'
         f'<p>Most domestic violence arrests in Dorchester County are heard by a magistrate at the Dorchester County Detention Center on Hodge Road in Summerville within 24 hours ({cite("bond", "S.C. Code § 22-5-510")}); Berkeley County hearings are at Hill-Finklea in Moncks Corner. The judge sets a bond and, almost always, a no-contact condition covering the other person and often the shared home. The alleged victim may be present and may speak. What you say at this hearing about the facts is evidence; what you say about your job, your residence and your record is what the judge needs.</p>'
         '<h2>Hour 24–48: going home—or not</h2>'
         '<p>If the bond order bars you from the residence, you cannot go back for clothes, medication or a vehicle without a police escort, arranged through the agency that made the arrest. Showing up anyway violates the bond, even if the other person invited you. That is mistake number one, and it is the most common one we see.</p>'
         '<h2>Hour 48–72: the phone</h2>'
         '<p>Mistake number two is the text message. “I\'m sorry,” “can we talk,” “please drop this”—each one is a bond violation and, depending on content, a possible witness-tampering charge. Mistake number three is the phone call from the jail, which is recorded. The other person\'s wishes matter to the prosecutor, but only the prosecutor can dismiss the case, and pressure on a witness makes dismissal less likely, not more.</p>'
         '<h2>What the charge actually is</h2>'
         f'<p>South Carolina grades domestic violence by injury, history and circumstances ({cite("cdv", "S.C. Code § 16-25-20")}), from third degree in magistrate or municipal court to first degree and high-and-aggravated in General Sessions. Any conviction carries a lifetime federal firearms prohibition. Our {A("domestic-violence-defense", "domestic violence defense page")} covers the degrees and the defenses.</p>'
         '<h2>If you are the person who was hurt</h2>'
         f'<p>This article is written for people who were arrested, but the same 72 hours are frightening from the other side. {link("my_sisters_house", "My Sister’s House")} serves Dorchester, Berkeley and Charleston counties with a 24-hour line, shelter and court advocacy, and the {link("dorchester_sheriff", "Dorchester County Sheriff’s Office")} victim advocates can explain the bond process and orders of protection.</p>'
         + callout("<b>Frost first:</b> if a family member calls you from the detention center, the most useful thing you can do is call a lawyer before the bond hearing—not post on Facebook, not call the other person, not “go get his things.”")
     ),
     sources=src("dorchester_sheriff", "my_sisters_house", "pc_summerville", "live5") + [("S.C. Code Title 16, Chapter 25 (domestic violence)", "https://www.scstatehouse.gov/code/t16c025.php", False)],
     related=["domestic-violence-defense", "bond-hearings", "arrest-warrants"],
     faqs=[("Can the victim drop domestic violence charges in South Carolina?", "No. Only the solicitor can dismiss a charge. The alleged victim's wishes are considered but do not control."),
           ("Can I get the no-contact order lifted?", "The court that set bond can modify it on motion, often after a cooling-off period and with the other person's input. Do not test it in the meantime.")])

# ----------------------------------------------------------------------------- 8. Berkeley County side of Summerville
post("summerville-address-berkeley-county-what-it-means", hero_image="cover-berkeley-line.jpg", hero_caption="The county line", author="tara", reviewer="jack", category="Probate",
     title="Summerville Address, Berkeley County: What It Means for Your Estate",
     description="Nexton, Cane Bay and Carnes Crossroads have Summerville addresses but sit in Berkeley County. That decides where your estate is probated, where a guardianship is filed and which court hears a ticket.",
     h1="Nexton, Cane Bay and Carnes Crossroads are in Berkeley County. Here is why that matters for your estate—and your speeding ticket",
     summary="The fastest-growing parts of “Summerville” are not in Dorchester County at all. The county line quietly decides which courthouse your family will deal with.",
     lead="Ask a Nexton resident what county they live in and you will get a pause. The mailing address says Summerville. The tax bill, the probate court and the sheriff say Berkeley.",
     body=(
         '<h2>The line</h2>'
         '<p>The Dorchester–Berkeley county line runs roughly along the old town\'s eastern and northern edges. The communities built since I-26\'s exit 197 opened—Nexton, Cane Bay, Carnes Crossroads, Sangaree, much of the 29486 ZIP code—are in Berkeley County. So is Jedburg. Historic downtown Summerville, Knightsville, Ashborough, Old Trolley Road and most of 29483 and 29485 are Dorchester County. Your property tax bill, your voter registration card and the county GIS map all say which side you are on.</p>'
         '<h2>What the county decides</h2>'
         + table(["Matter", "Dorchester side", "Berkeley side"], [
             ["Probate of an estate", "Dorchester County Probate Court, St. George", "Berkeley County Probate Court, Moncks Corner"],
             ["Guardianship or conservatorship", "Dorchester County Probate Court", "Berkeley County Probate Court"],
             ["Recording a deed or power of attorney", "Dorchester County Register of Deeds", "Berkeley County Register of Deeds"],
             ["A traffic stop by the sheriff or Highway Patrol", "Dorchester County magistrate", "Berkeley County magistrate"],
             ["A felony charge", "Dorchester County General Sessions, St. George", "Berkeley County General Sessions, Moncks Corner"],
             ["Bond hearing after arrest", "Dorchester County Detention Center, Hodge Road, Summerville", "Hill-Finklea Detention Center, Moncks Corner"],
         ]) +
         '<p>Inside the Summerville town limits—which also cross the county line—Summerville Municipal Court hears town-police tickets and ordinance cases regardless of county.</p>'
         '<h2>Why it matters for planning</h2>'
         f'<p>Estates are probated where the person was domiciled at death, so a Cane Bay retiree\'s estate goes to Moncks Corner even though every relative assumes Dorchester. A durable power of attorney is recorded in the county of residence. And when families file in the wrong court, the case is dismissed and refiled—weeks lost during a hard time. Our {A("probate-courts", "guide to the three probate courts")} has addresses and phones for each.</p>'
         '<h2>Why it matters for a charge</h2>'
         f'<p>Which sheriff\'s office made the arrest and which solicitor\'s office prosecutes are county questions too, although Dorchester and Berkeley share the First Judicial Circuit solicitor. Jack appears in both counties\' courts; see {A("service-areas/nexton", "Nexton")}, {A("service-areas/cane-bay", "Cane Bay")} and {A("service-areas/carnes-crossroads", "Carnes Crossroads")} for the specifics.</p>'
         + callout("<b>Frost first:</b> if you are opening an estate for someone who lived in a 29486 address, check the county before you file anything. It is the single most common wrong-court filing we see.")
     ),
     sources=src("berkeley_county", "dorchester_county", "berkeley_probate_site", "dorchester_probate_site"),
     related=["probate-courts", "service-areas/nexton", "service-areas/cane-bay"],
     faqs=[("Is Nexton in Dorchester or Berkeley County?", "Berkeley County, with a Summerville mailing address (ZIP 29486)."),
           ("Which probate court handles a Cane Bay estate?", "Berkeley County Probate Court in Moncks Corner.")])


# ============================================================================= November 2026 posts
NOV = "2026-11-13"

# ----------------------------------------------------------------------------- 9. Eviction notices
post("south-carolina-eviction-notice-5-day-14-day-30-day", date=NOV, hero_image="summerville-downtown.jpg", hero_caption="Downtown Summerville", author="tara", reviewer="jack", category="Landlord-tenant",
     title="South Carolina Eviction Notices: The 5-Day, 14-Day and 30-Day Notice, With Sample Wording",
     description="What each South Carolina eviction notice must say, when the Residential Landlord and Tenant Act requires it, how to deliver it, and sample wording for the five-day, fourteen-day and thirty-day notices.",
     h1="South Carolina Eviction Notices: The 5-Day, 14-Day and 30-Day Notice, With Sample Wording",
     summary="Most evictions that fail in magistrate court fail at the notice. What each notice must say, when it is required, how to deliver it, and wording you can adapt.",
     lead="A former magistrate’s view of the piece of paper that decides most eviction hearings: which notice South Carolina requires for which situation, what it has to say, and how to prove you gave it.",
     body=(
         answer(f"South Carolina requires three different notices depending on why the tenant is being evicted. For unpaid rent, written notice and five days to pay ({cite('rlta', 'S.C. Code § 27-40-710(B)')}), unless the written lease says in conspicuous language that nonpayment is itself the notice. For any other lease violation, a written notice describing the violation and giving fourteen days to cure it (§ 27-40-710(A)). To end a month-to-month tenancy, written notice at least thirty days before the termination date (§ 27-40-770), seven days for a week-to-week tenancy. A fixed-term lease that has ended needs no statutory notice. The notice must be in writing, must be delivered so you can prove it, and must be accurate, because an error in the amount, the dates or the names is the tenant’s best defense.", "The short answer")
         + '<h2>Which notice, for which situation</h2>'
         + table(["Situation", "Notice required", "Statute"], [
             ["Rent unpaid", "Written notice of nonpayment and intent to terminate, with five days to pay. A written lease that states in bold, conspicuous type that nonpayment constitutes notice satisfies this for the whole term.", "§ 27-40-710(B); § 27-37-10(B)"],
             ["Any other lease violation: unauthorized occupants, pets, damage, nuisance, unsanitary conditions", "Written notice specifying the acts or omissions and stating that the lease terminates on a date at least fourteen days after receipt unless the breach is cured.", "§ 27-40-710(A)"],
             ["Ending a month-to-month tenancy for any reason or none", "Written notice at least thirty days before the termination date stated in the notice.", "§ 27-40-770(b)"],
             ["Ending a week-to-week tenancy", "Written notice at least seven days before the termination date.", "§ 27-40-770(a)"],
             ["Lease term has ended and the tenant stays", "No statutory notice; the tenant is a holdover. Check the lease for automatic renewal language first.", "§ 27-40-770"],
         ]) +
         f'<p>The notice is the first step of the {A("south-carolina-eviction-process", "South Carolina eviction process")}; the Application for Ejectment, the Rule to Vacate or Show Cause and the writ follow it. Nothing below replaces reading your own lease, which can require more notice than the statute, never less.</p>'
         '<h2>The five-day notice for unpaid rent</h2>'
         '<p>Rent is due on the day the lease says. The Act lets the landlord terminate if the rent is not paid within five days after it is due, provided the tenant has been given written notice of the nonpayment and of the landlord’s intention to terminate. The lease clause most Lowcountry landlords use, printed in bold, says that nonpayment within five days of the due date is itself notice; with that clause, no separate letter is required and the application can be filed on the sixth day. Without the clause, or with no written lease at all, you must send this notice and wait the five days.</p>'
         + callout("<b>Sample wording.</b> NOTICE OF NONPAYMENT OF RENT AND INTENT TO TERMINATE. To [every adult tenant by name], [address of the unit]. Rent of $[amount] for [period] was due on [date] and has not been paid. Under S.C. Code § 27-40-710(B), you have five (5) days from delivery of this notice to pay the full amount owed. If it is not paid within five days, your rental agreement will terminate and the landlord will apply to the magistrate court for ejectment. Delivered on [date] by [hand delivery / posting at the unit and first-class mail]. [Landlord or agent name, address, phone].")
         + '<p>Name the exact amount of rent due, not a running total that includes late fees the lease does not authorize. Count the five days from the day the notice is delivered, not the day it was typed. Name every adult on the lease.</p>'
         '<h2>The fourteen-day notice to cure</h2>'
         '<p>For a breach other than rent, the Act requires a notice that specifies the acts and omissions constituting the breach and states that the rental agreement will terminate on a date not less than fourteen days after receipt if the breach is not remedied. If the tenant fixes the problem before that date, the tenancy continues. If the fix cannot be completed in fourteen days but is started and pursued in good faith, the lease does not terminate. Vague notices lose: “violation of lease” is not a specification; “an unauthorized adult has lived in the unit since October 1, in violation of paragraph 9” is.</p>'
         + callout("<b>Sample wording.</b> NOTICE OF LEASE VIOLATION AND INTENT TO TERMINATE. To [tenant names], [address]. You are in violation of paragraph [number] of your rental agreement because [specific facts, with dates]. Under S.C. Code § 27-40-710(A), you have fourteen (14) days from receipt of this notice to correct the violation. If it is not corrected, your rental agreement will terminate on [a date at least fourteen days after the tenant receives the notice] and the landlord will apply to the magistrate court for ejectment. Delivered on [date] by [method]. [Landlord or agent name, address, phone].")
         + '<h2>The thirty-day notice that ends a month-to-month tenancy</h2>'
         '<p>No reason is required to end a periodic tenancy, only timing: the notice must be given at least thirty days before the termination date it names. Tie the termination date to the end of a rental period so there is no argument about prorated rent, and remember that the same rule binds the tenant who wants to leave. A tenant who stays past the date is a holdover, and a willful holdover can owe up to three months’ rent or twice the landlord’s actual damages plus attorney’s fees.</p>'
         + callout("<b>Sample wording.</b> NOTICE OF TERMINATION OF MONTH-TO-MONTH TENANCY. To [tenant names], [address]. Your month-to-month tenancy will terminate on [date at least thirty days after delivery, ideally the last day of a rental period]. Under S.C. Code § 27-40-770, this notice is given more than thirty days before that date. Please deliver possession of the premises and all keys by that date and provide a forwarding address for the return of your security deposit under § 27-40-410. Delivered on [date] by [method]. [Landlord or agent name, address, phone].")
         + '<h2>How to deliver a notice so the magistrate accepts it</h2>'
         + checks(["<b>Hand it to the tenant</b> when you can, and note the date, time and who was present.",
                   "<b>If no one is home,</b> post it on the door and mail a copy by first-class mail the same day, keeping a photograph of the posted notice and a certificate of mailing.",
                   "<b>Keep a dated copy</b> of every notice, the lease and the rent ledger; these three documents are the landlord’s case.",
                   "<b>Text messages and e-mail</b> are useful as a record but risky as the only notice unless the lease expressly allows electronic notice. Paper first, text second.",
                   f"<b>Dorchester County’s magistrates</b> publish a Notice to Quit and an eviction packet on the {ext('https://www.dorchestercountysc.gov/government/courts-judicial-services/magistrate-court', 'county’s magistrate court page')}; the statewide forms are on the Judicial Branch’s forms site."]) +
         '<h2>The mistakes we see from the bench</h2>'
         + checks(["Filing on day four because the rent was due “on the first” and the calendar was misread",
                   "A notice that demands rent plus late fees, a returned-check charge and the water bill, when only rent was due",
                   "A fourteen-day notice that names no cure period, or a termination date twelve days out",
                   "Only one of two tenants named, so the writ does not cover the other",
                   "No proof of delivery at all, which turns the hearing into a credibility contest the landlord often loses"]) +
         '<h2>If you are the tenant</h2>'
         f'<p>Read the notice against the table above. A notice with the wrong amount, the wrong period or no delivery you can be shown is a defense to raise at the hearing, and you must request that hearing within ten days of being served with the Rule to Vacate. If the notice is correct and you can pay within the period, pay, get a dated receipt, and keep a copy of everything. If you are moving out, give a written forwarding address so the thirty-day clock on your {A("south-carolina-security-deposit-law", "security deposit")} starts.</p>'
         + callout(f"<b>Frost first:</b> a landlord should have us read the lease and the notice before filing, and a tenant should call the day the rule is served. Both calls take ten minutes; a lost hearing costs a month. Details on our {A('eviction-lawyer-summerville-sc', 'landlord-tenant page')} or call {TEL}.")
     ),
     sources=[("S.C. Code § 27-40-10 et seq. (Residential Landlord and Tenant Act)", "https://www.scstatehouse.gov/code/t27c040.php", False),
              ("S.C. Code § 27-37-10 et seq. (ejectment)", "https://www.scstatehouse.gov/code/t27c037.php", False),
              ("Dorchester County Magistrate Court forms", "https://www.dorchestercountysc.gov/government/courts-judicial-services/magistrate-court", False)],
     related=["south-carolina-eviction-process", "eviction-lawyer-summerville-sc", "south-carolina-security-deposit-law"],
     faqs=[("How much notice does a landlord have to give before evicting in South Carolina?", "Five days for unpaid rent after written notice (or none, if the lease says in conspicuous type that nonpayment is notice), fourteen days to cure any other lease violation, and thirty days to end a month-to-month tenancy. A fixed-term lease that has ended needs no statutory notice."),
           ("Can an eviction notice be sent by text or e-mail in South Carolina?", "The Act requires written notice and counts it as given when it is delivered. A text or e-mail is a useful record, but unless the lease expressly allows electronic notice, deliver it on paper by hand or by posting and mail, and keep proof."),
           ("Do I still need a five-day notice if my lease says nonpayment is notice?", "No. A written lease that states in bold, conspicuous language that nonpayment within five days of the due date constitutes notice satisfies the requirement for the whole term. Without that clause, or without a written lease, send the notice and wait the five days.")])

# ----------------------------------------------------------------------------- 10. HCPOA vs living will
post("health-care-power-of-attorney-vs-living-will-south-carolina", date=NOV, hero_image="estate-plan.jpg", hero_caption="A complete plan: health care directive, will, trust, power of attorney", author="tara", reviewer="jack", category="Estate planning",
     title="Health Care Power of Attorney vs. Living Will in South Carolina: Which One Do You Need?",
     description="The difference between a South Carolina health care power of attorney and a living will, who makes medical decisions if you have neither, the signing rules for each, and why most people sign both in one meeting.",
     h1="Health Care Power of Attorney vs. Living Will in South Carolina: Which One Do You Need?",
     summary="One names a person; the other states your wishes. They are signed differently, they apply in different situations, and the Adult Health Care Consent Act decides who speaks for you if you have neither.",
     lead="Clients ask this every week, usually after a hospital hands a relative a form. The two documents are not interchangeable, and the gap between them is where families end up arguing in a hallway.",
     body=(
         answer(f"A South Carolina health care power of attorney names a person, your agent, to make any medical decision you cannot make yourself, from consenting to surgery to choosing a facility ({cite('hcpoa', 'S.C. Code §§ 62-5-503 and 62-5-504')}). A living will, formally a Declaration of a Desire for a Natural Death, is your own written instruction that life-sustaining treatment be withheld or withdrawn if you are terminally ill or permanently unconscious ({cite('living_will_act', 'S.C. Code § 44-77-10 et seq.')}). The agent decides everything the living will does not cover; the living will binds your providers in the one situation it covers, even if your agent cannot be reached. Most people need both, and they are signed in the same meeting.", "The short answer")
         + '<h2>Side by side</h2>'
         + table(["", "Health care power of attorney", "Living will"], [
             ["What it is", "Appoints a person to decide for you", "States your own decision in advance"],
             ["When it applies", "Any time you cannot make or communicate a health care decision", "Only when two physicians certify a terminal condition or permanent unconsciousness and you cannot decide"],
             ["What it covers", "Every medical decision: treatment, providers, facilities, records, end-of-life care consistent with your wishes", "Life-sustaining procedures and, if you choose, artificial nutrition and hydration"],
             ["Signing rules", "Two qualified witnesses; notary optional under the statutory form", "Notary and two qualified witnesses; an ombudsman witness if signed in a hospital or nursing home"],
             ["Can be revoked", "Any time you have capacity, in writing or by signing a new one", "Any time, in any way that shows your intent"],
             ["Weak spot", "Useless if the agent cannot be found or will not decide", "Silent on everything short of the end of life"],
         ]) +
         '<h2>Why the health care power of attorney does more</h2>'
         f'<p>The {A("power-of-attorney", "health care power of attorney")} is the document that gets used. A stroke, a car crash on I-26, sedation after surgery, dementia: in each of them someone has to consent to treatment, talk to the physicians, choose between rehabilitation facilities and decide when to bring you home. South Carolina’s statutory form also includes a section in which you state your desires about life-sustaining treatment and tube feeding, so your agent has written guidance rather than a guess. Your agent must be an adult who is not your health care provider or the provider’s employee, and you should name a successor.</p>'
         '<h2>Why you still want the living will</h2>'
         f'<p>The {A("living-will", "living will")} speaks directly to the hospital in the narrow situation the statute covers, and it does so whether or not your agent is in the building, awake, or emotionally able to say the words. It also protects the agent: a daughter who can point to her mother’s signed declaration is not the one “deciding” to stop treatment. For couples who name each other as agent, the living will matters even more, because the agent is often the person sitting in the same emergency room.</p>'
         '<h2>What happens if you have neither</h2>'
         f'<p>South Carolina’s Adult Health Care Consent Act ({ext("https://www.scstatehouse.gov/code/t44c066.php", "S.C. Code § 44-66-30")}) supplies a decision-maker in order of priority: a court-appointed guardian, then an agent under a health care power of attorney, then a spouse unless legally separated, then a parent or adult child, then an adult sibling, grandparent or adult grandchild, then other relatives and persons with a close relationship. The list works until it does not: three adult children with equal standing and different views, a second spouse and children from a first marriage, or a partner of twenty years who is not on the list at all. Without documents, the only way to settle those disputes is a {A("guardianship-and-conservatorship", "guardianship")} in probate court, which takes months and is public.</p>'
         '<h2>Signing both correctly</h2>'
         + checks(["<b>Health care power of attorney:</b> dated and signed by you before two witnesses who are not related to you, not responsible for your medical bills, not your heirs or beneficiaries, not your agent, and not your attending physician or the physician’s employee. No more than one witness may work for the facility where you are a patient. We notarize it anyway so it travels well to other states.",
                   "<b>Living will:</b> dated and signed before a notary and two witnesses with the same disqualifications, one of whom may be the notary. If you sign as a patient in a hospital or a resident of a nursing home, one witness must be an ombudsman designated by the State Ombudsman.",
                   "<b>Copies:</b> to your agent, your physicians and the hospital system you use (Summerville Medical Center, Trident, Roper St. Francis, MUSC) so they are in your chart before a crisis."]) +
         '<h2>Which first, if you only sign one today</h2>'
         f'<p>The health care power of attorney, because it covers everything and the living will covers one thing. But the honest answer is that both take one short meeting, both are included in every {A("estate-planning-attorney", "estate plan")} we prepare, and a plan with one and not the other leaves either the agent or the hospital guessing at the worst moment. If your documents are from another state or from before 2017, a {A("estate-plan-review", "plan review")} will tell you whether they need to be re-signed here.</p>'
         + callout("<b>Frost first:</b> if a hospital or facility hands your family a health care form to sign at the bedside, call before anyone signs. The witness rules are strict, and a document that fails them is set aside exactly when it is needed.")
     ),
     sources=[("S.C. Code §§ 62-5-503 and 62-5-504 (health care power of attorney)", "https://www.scstatehouse.gov/code/t62c005.php", False),
              ("S.C. Code § 44-77-10 et seq. (Death with Dignity Act)", "https://www.scstatehouse.gov/code/t44c077.php", False),
              ("S.C. Code § 44-66-10 et seq. (Adult Health Care Consent Act)", "https://www.scstatehouse.gov/code/t44c066.php", False)],
     related=["power-of-attorney", "living-will", "estate-plan-review"],
     faqs=[("Does a living will replace a health care power of attorney in South Carolina?", "No. A living will only addresses life-sustaining treatment when you are terminally ill or permanently unconscious. A health care power of attorney names a person to make every other medical decision. You need both."),
           ("Does a South Carolina health care power of attorney have to be notarized?", "No. The statutory form requires two qualified witnesses and makes the notary acknowledgment optional. We notarize it anyway so it is accepted without question in other states."),
           ("Who makes medical decisions in South Carolina if I have no documents?", "The Adult Health Care Consent Act sets the order: a guardian, then a health care agent, then a spouse, then a parent or adult child, then an adult sibling, grandparent or adult grandchild, then other relatives and close persons. Disputes among people of equal rank end up in probate court.")])

# ----------------------------------------------------------------------------- 11. Small estate limit
post("south-carolina-small-estate-limit-45000", date=NOV, hero_image="nest-egg.jpg", hero_caption="A modest estate", author="tara", reviewer="jack", category="Probate",
     title="South Carolina Raised the Small Estate Limit to $45,000. Here Is Who Can Skip Probate Now",
     description="Act 26 of 2025 raised South Carolina’s small estate affidavit limit from $25,000 to $45,000 on May 8, 2025. Who qualifies now, what the affidavit costs in Dorchester, Berkeley and Charleston County, and when an estate still needs probate.",
     h1="South Carolina Raised the Small Estate Limit to $45,000. Here Is Who Can Skip Probate Now",
     summary="The ceiling for collecting an estate by affidavit nearly doubled in May 2025. More Lowcountry families now qualify, and most do not know it.",
     lead="For eleven years a South Carolina estate had to be under $25,000 to skip probate with an affidavit. Since May 8, 2025, the number is $45,000. Here is what changed, who it helps, and what it still does not do.",
     body=(
         answer(f"Act 26 of 2025 amended {cite('small_estate', 'S.C. Code § 62-3-1201')} to raise the small estate affidavit ceiling from $25,000 to $45,000, effective May 8, 2025, and made the same change to summary administration under § 62-3-1203. If the probate estate, meaning everything passing under the will or by intestacy, less liens, is $45,000 or less, a successor can collect the decedent’s personal property with Form 420ES thirty days after death instead of opening an estate. Real estate still cannot pass by affidavit, and the filing fee is $25 to $67.50 depending on the value.", "The short answer")
         + '<h2>What changed, exactly</h2>'
         f'<p>The General Assembly passed H.3472 in the 2025 session and the Governor signed it as {ext("https://www.scstatehouse.gov/sess126_2025-2026/bills/3472.htm", "Act No. 26 of 2025")}. Section 1 substituted “forty-five thousand dollars” for “twenty-five thousand dollars” in § 62-3-1201, the affidavit statute, and Section 2 did the same in § 62-3-1203, which lets a personal representative close a small estate with a verified closing statement after notice to creditors. The previous ceiling had been in place since January 1, 2014. Nothing else about the procedure changed: thirty days must pass after death, no personal representative may be appointed or applied for, the affidavit must be approved and countersigned by the probate judge of the county where the person lived, and the person collecting holds the property for the heirs and creditors.</p>'
         '<h2>Who qualifies now and did not before</h2>'
         + table(["Family situation", "Under the old $25,000 limit", "Under the $45,000 limit"], [
             ["Checking and savings of $32,000 in Dad’s name alone; house owned jointly with Mom", "Full probate for the accounts", "Affidavit; the house passes to Mom by survivorship"],
             ["A paid-off 2019 truck worth $21,000 and a $19,000 brokerage account with no beneficiary", "Full probate", "Affidavit for both"],
             ["$40,000 in accounts plus a $150,000 house titled only in the decedent’s name", "Full probate", "Still full probate; the house cannot pass by affidavit"],
             ["$60,000 in accounts, no real estate", "Full probate", "Full probate, but summary administration may close it quickly"],
         ]) +
         '<p>Assets that pass outside probate were never part of the calculation and still are not: life insurance and retirement accounts with named beneficiaries, joint accounts and real estate with survivorship, payable-on-death accounts and anything in a trust. The number that matters is what was in the decedent’s name alone with no beneficiary.</p>'
         '<h2>What it costs and how long it takes</h2>'
         f'<p>The affidavit fee follows the estate fee schedule in {cite("probate_fees", "S.C. Code § 8-21-770")}: $25 for property under $5,000, $45 up to $20,000 and $67.50 from $20,000 to $45,000, plus $5 per certified copy. You must wait thirty days after the death, and the court’s review and the judge’s signature usually take a few days to two weeks. Each county has its own intake: {A("dorchester-county-probate-court", "Dorchester County")} asks families filing without a lawyer to complete its Opening Probate Worksheet first, {A("berkeley-county-probate-court", "Berkeley County")} takes walk-ins at the counter until 3:30, and {A("charleston-county-probate-court", "Charleston County")} accepts filings through EZ-Filing and by appointment. The {A("small-estate-affidavit", "small estate affidavit page")} walks through the form line by line.</p>'
         '<h2>What the new limit does not do</h2>'
         + checks(["It does not move real estate. A house, a lot or an interest in family land titled in the decedent’s name alone needs a deed of distribution through an estate, even when nothing else is owned.",
                   "It does not resolve disputes. An affidavit is a sworn statement that the signer is entitled to the property; when heirs disagree or a will does not match the intestacy shares, open the estate.",
                   "It does not protect the signer from creditors. The person who collects remains answerable to creditors and other heirs for what was collected.",
                   "It does not shorten the creditor period for summary administration, which still requires published notice and runs eight months."]) +
         '<h2>Deaths before May 2025</h2>'
         '<p>Families sometimes discover an account years after a death. If the death was before May 8, 2025 and no estate was ever opened, ask before assuming which ceiling applies; the answer has turned on when the affidavit is presented, and the court will tell you what it will accept. Estates can be opened up to ten years after death.</p>'
         + callout(f"<b>Frost first:</b> the bank will not tell you whether an affidavit is the right tool; it will accept it or reject it. Tell us what was owned and how it was titled and we will tell you in ten minutes whether your family qualifies under the new limit. {TEL}")
     ),
     sources=[("S.C. Code § 62-3-1201 (collection of personal property by affidavit)", "https://www.scstatehouse.gov/code/t62c003.php", False),
              ("2025 Act No. 26 (H.3472)", "https://www.scstatehouse.gov/sess126_2025-2026/bills/3472.htm", False),
              ("S.C. Code § 8-21-770 (probate fees)", "https://www.scstatehouse.gov/code/t08c021.php", False)],
     related=["small-estate-affidavit", "probate-process", "dorchester-county-probate-court"],
     faqs=[("What is the small estate limit in South Carolina in 2026?", "$45,000, measured by the probate estate less liens. Act 26 of 2025 raised it from $25,000 effective May 8, 2025."),
           ("Does the $45,000 limit include the house?", "A house titled jointly with survivorship passes outside probate and is not counted. A house titled in the decedent’s name alone cannot pass by affidavit at all, so the estate must be opened regardless of the other numbers."),
           ("What form do I use for a small estate in South Carolina?", "Form 420ES, the Affidavit for Collection of Personal Property Pursuant to Small Estate Proceedings, filed with the probate court of the county where the decedent lived, with the original will if there is one and a certified death certificate.")])

# ----------------------------------------------------------------------------- 12. Unpaid ticket chain
post("unpaid-ticket-bench-warrant-suspended-license-south-carolina", date=NOV, hero_image="county-dorchester.jpg", hero_caption="Dorchester County", author="jack", reviewer="tara", category="Criminal defense",
     title="How an Unpaid Ticket in South Carolina Becomes a Bench Warrant and a Suspended License",
     description="How a missed court date on a South Carolina traffic ticket becomes a bench warrant and a DMV suspension, what driving on that suspension costs under § 56-1-460, and how to unwind the chain before holiday travel.",
     h1="How an Unpaid Ticket in South Carolina Becomes a Bench Warrant and a Suspended License",
     summary="A $200 ticket ignored in March is an arrest at a traffic stop in December. A former officer explains each link in the chain and how to break it.",
     lead="Every holiday season Jack gets the same call from the side of I-26: a routine stop, a name run, a bench warrant from a ticket nobody remembered. The chain from ticket to handcuffs is predictable, and every link can be undone, in order.",
     body=(
         answer(f"A South Carolina traffic ticket is a summons to court. Pay it and you have pleaded guilty, with the points that follow. Ignore it and miss the court date and the magistrate or municipal judge issues a bench warrant for failure to appear and notifies the Department of Motor Vehicles, which suspends your license under {ext('https://www.scstatehouse.gov/code/t56c025.php', 'S.C. Code § 56-25-20')} until the court certifies that the ticket has been resolved and you pay a $100 reinstatement fee for each suspension. Drive in the meantime and you can be charged with {A('traffic-tickets', 'driving under suspension')}, a separate criminal offense with its own fine, jail exposure and added suspension. The way out is to resolve the ticket, have the warrant recalled, get the court’s compliance notice to the DMV and pay the reinstatement fee, in that order.", "The short answer")
         + '<h2>The chain, link by link</h2>'
         + steps([
             ("The ticket.", " A uniform traffic ticket from the Highway Patrol, a sheriff’s deputy or a town officer sets a court date at the magistrate or municipal court for where the stop happened: the Summerville magistrate on Deming Way or Summerville Municipal Court for most local stops, St. George for upper Dorchester County, the Berkeley County magistrates for Goose Creek and Moncks Corner, and the Charleston County courts for North Charleston and the islands."),
             ("Paying is pleading.", " Paying the fine online or by mail is a guilty plea. The points post to your record, your insurer sees them at renewal, and some offenses carry a suspension on their own. Requesting a court date instead costs nothing and is often where a reduction happens."),
             ("The missed date.", " If you neither pay nor appear, the judge issues a bench warrant for failure to appear. Some courts try the ticket in your absence and enter a conviction with the maximum fine."),
             ("The DMV suspension.", " The court reports the failure to comply to the DMV, which suspends your license until it receives notice from the court that you have paid or appeared. The suspension letter goes to the address on your license, which is one reason so many people learn about it from an officer."),
             ("The traffic stop.", " An active bench warrant means arrest on the spot, a trip to the detention center and a bond hearing, usually within twenty-four hours. If you were driving on the suspended license, a driving under suspension charge is added."),
             ("Driving under suspension.", f" Under {ext('https://www.scstatehouse.gov/code/t56c001.php', 'S.C. Code § 56-1-460')} a first offense carries a $300 fine or up to 30 days in jail, a second $600 or up to 60 days, and a third $1,000 and up to 90 days or home detention, and each conviction extends the suspension. Traffic offenses, including this one, are excluded from expungement."),
         ]) +
         '<h2>Breaking the chain</h2>'
         + checks([f"<b>Find out where you stand.</b> Search the county public index for the ticket and its status, or let us call the clerk. Our {A('arrest-warrants', 'warrants page')} lists the Dorchester, Berkeley and Charleston County records and the sheriffs’ warrants units, and explains why calling in your own name is not always wise.",
                   "<b>Resolve the ticket.</b> Depending on the court and how old the ticket is, that means paying it, appearing and pleading, or having us file a motion to recall the bench warrant and reset the case so the charge itself can still be contested or reduced.",
                   "<b>Get the compliance notice to the DMV.</b> The court transmits it once the case is resolved; ask for a copy. Nothing happens at the DMV until it arrives.",
                   f"<b>Pay the reinstatement fee.</b> $100 per suspension under {ext('https://www.scstatehouse.gov/code/t56c001.php', 'S.C. Code § 56-1-390')}, payable at a DMV branch or, in some cases, to the clerk when the ticket is resolved. The DMV also runs a payment program for people who owe several fees.",
                   "<b>Check your record before you drive.</b> A clear court file and an unpaid reinstatement fee still equal a suspended license. Confirm reinstatement on the DMV’s site before the next trip."]) +
         '<h2>Out-of-state drivers and out-of-state tickets</h2>'
         '<p>South Carolina reports unresolved tickets to a driver’s home state under the interstate compacts, so a ticket from a beach trip to Folly or a drive through Dorchester County on I-26 can suspend a Georgia or North Carolina license months later. The fix is the same: resolve the South Carolina ticket first, then clear the home-state suspension with proof.</p>'
         '<h2>Before Thanksgiving and Christmas travel</h2>'
         f'<p>If there is any chance an old ticket is out there, check now rather than at a checkpoint on the way to a relative’s house. A bench warrant discovered on a holiday weekend means a bond hearing before a magistrate at the detention center and a night most people would rather not explain. Our {A("bond-hearings", "bond hearings page")} explains what happens if it comes to that; a phone call this week usually means it does not.</p>'
         + callout(f"<b>Frost first:</b> do not drive to the courthouse on a suspended license to fix a suspended license. Call first. We can often recall the warrant and resolve the ticket without you appearing, and we will tell you when it is lawful to drive again. {TEL}")
     ),
     sources=[("S.C. Code § 56-25-20 (suspension for failure to comply with a traffic citation)", "https://www.scstatehouse.gov/code/t56c025.php", False),
              ("S.C. Code § 56-1-460 (driving under suspension) and § 56-1-390 (reinstatement fee)", "https://www.scstatehouse.gov/code/t56c001.php", False),
              ("SCDMV: paying reinstatement fees", "https://dmv.sc.gov/driver-services/license-reinstatement/pay-reinstatement-fees", False)],
     related=["traffic-tickets", "arrest-warrants", "bond-hearings"],
     faqs=[("Does an unpaid traffic ticket turn into a warrant in South Carolina?", "Yes. A ticket is a summons to court; if you neither pay it nor appear, the judge issues a bench warrant for failure to appear and reports the failure to the DMV, which suspends your license."),
           ("How much is the reinstatement fee for a suspended license in South Carolina?", "$100 for each suspension on your record, paid to the DMV after the court certifies that the ticket has been resolved. The DMV offers a payment program for drivers who owe several fees."),
           ("Can I just pay the old ticket online to clear the warrant?", "Sometimes, and sometimes paying enters a conviction with points you could have avoided. Have the clerk or a lawyer check whether the court will accept payment on an outstanding bench warrant and whether a court appearance would get the charge reduced instead.")])
