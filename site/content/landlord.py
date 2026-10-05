"""Landlord-tenant hub and spokes: evictions (ejectment), the South Carolina eviction process, security deposits.

Evictions are heard by the magistrate; Tara Frost served as a Dorchester County Magistrate Judge (2022–2025).
Statute links come from the verified local data (local.cite)."""
from .base import page, A, ext, img, p, ul, checks, steps, callout, answer, band, esc, table
from . import firm
from .local import cite, link

HUB = "eviction-lawyer-summerville-sc"
TEL = f'<a href="tel:{firm.PHONE_E164}">{firm.PHONE}</a>'


def sp(slug, **kw):
    kw.setdefault("kind", "spoke")
    kw.setdefault("hub", HUB)
    kw.setdefault("eyebrow", "Landlord-tenant · Summerville, SC")
    return page(slug, **kw)


# ----------------------------------------------------------------------------- HUB
hub_body = (
    answer("Frost Law Group represents landlords and tenants in the Dorchester, Berkeley and Charleston County magistrate courts: evictions (which South Carolina law calls ejectment) for nonpayment, lease violations and holdovers; defense of tenants who were never properly notified or whose landlord ignored the Residential Landlord and Tenant Act; security deposit claims; and lease drafting and review. Every eviction in South Carolina is heard by a magistrate, and Tara Frost served as a Dorchester County Magistrate Judge from 2022 to 2025.", "Who handles evictions and landlord-tenant cases in Summerville, SC?")
    + '<h2>The law that governs rentals here</h2>'
    f'<p>Residential rentals in South Carolina are governed by the {cite("rlta", "Residential Landlord and Tenant Act, S.C. Code § 27-40-10 et seq.")}, and evictions follow the ejectment statute, {cite("ejectment", "S.C. Code § 27-37-10 et seq.")}, in the magistrate court of the county where the property is. The Act sets the landlord’s duty to keep the unit fit and habitable, the tenant’s duty to pay rent and keep the unit clean and undamaged, the notices each side must give, the thirty-day security deposit rule and the twenty-four-hour entry rule. It does not apply to hotel stays, owner-occupied condominium units, farm leases or housing provided to an employee as part of the job.</p>'
    '<h2>For landlords</h2>'
    + checks([
        f"<b>Evictions done right the first time.</b> The Application for Ejectment, service of the Rule to Vacate or Show Cause, the hearing if the tenant requests one, the Writ of Ejectment and its execution by the constable or deputy. A defective notice or a misstatement in the application sends you back to the beginning, with another month of unpaid rent. Our {A('south-carolina-eviction-process', 'step-by-step guide to the South Carolina eviction process')} explains each stage.",
        "<b>The right notice for the right ground.</b> For nonpayment, the Act requires written notice and five days to pay, which a lease satisfies permanently if it says so in conspicuous language; for other lease violations, a written fourteen-day notice to cure; for a month-to-month tenancy, thirty days’ written notice; for a holdover after the lease ends, no notice at all. We check the lease before we file so the ground and the notice match.",
        f"<b>Money judgments.</b> Unpaid rent, late fees the lease allows and damage beyond normal wear can be claimed in the same magistrate court up to its {cite('magistrate_civil', '$7,500 civil limit')}, and a willful holdover tenant owes up to three months’ rent or twice your actual damages, whichever is greater, plus attorney’s fees.",
        "<b>Leases written for the Act.</b> A bold nonpayment-notice clause, a regularly-scheduled-services entry clause, deposit terms that match the thirty-day rule, pet and HOA provisions, and the disclosures the Act requires. A good lease is the cheapest eviction you will ever buy.",
        "<b>Deposits and abandoned property.</b> How to itemize and return a deposit within thirty days, and what the Act lets you do with belongings a tenant leaves behind.",
        f"<b>What you cannot do.</b> Changing the locks, shutting off utilities, removing doors or belongings, or threatening to, without a writ. The Act gives a tenant who is unlawfully put out three months’ rent or twice actual damages, whichever is greater, plus attorney’s fees, and a magistrate who sees self-help in the file remembers the landlord’s name."]) +
    '<h2>For tenants</h2>'
    + checks([
        "<b>Facing an eviction.</b> Once you are served with a Rule to Vacate or Show Cause you have ten days to ask the magistrate for a hearing. Do nothing and the writ issues. At the hearing, defenses include a notice that was never given or was given wrong, rent that was tendered and refused before the case was filed, a landlord who failed to make repairs after written notice, retaliation for a complaint to code enforcement, or a case filed against the wrong person. You may demand a jury.",
        f"<b>Security deposits.</b> A landlord has thirty days after you move out, return the keys and ask for it to return your deposit with an itemized list of any deductions, and a landlord who wrongfully withholds it owes three times the amount plus attorney’s fees. Our {A('south-carolina-security-deposit-law', 'security deposit page')} explains how to make the demand and where to sue.",
        "<b>Repairs.</b> When a landlord ignores a condition that affects health or safety, the Act lets you give written notice that the lease will end in fourteen days if it is not fixed, recover damages, and in limited cases of no heat, water or other essential services, obtain them yourself and deduct the reasonable cost. The notice has to be in writing, specific and delivered the right way, and we draft it.",
        "<b>Privacy.</b> A landlord must give twenty-four hours’ notice before entering and may enter only at reasonable times, except in an emergency or for regularly scheduled services disclosed in the lease, which must be done between 9 AM and 6 PM after announcing the entry.",
        "<b>Ending a lease early.</b> Military orders, a landlord’s material breach, or a negotiated surrender. We tell you what an early exit will actually cost before you hand over the keys."]) +
    '<h2>How an eviction works in South Carolina, briefly</h2>'
    + steps([
        ("Ground and notice.", " Nonpayment after the five-day period, a lease violation after a fourteen-day cure notice, the end of the term, or thirty days’ notice on a month-to-month tenancy."),
        ("Application for Ejectment.", " Filed by the landlord in the magistrate court for the county where the property is, with a $40 filing fee plus a small fee for the writ. The magistrate issues a Rule to Vacate or Show Cause, which a constable or deputy serves on the tenant."),
        ("Ten days.", " The tenant has ten days after service to request a hearing. No request, and the magistrate issues the Writ of Ejectment."),
        ("The hearing.", " Usually within a few weeks. Either side may demand a jury. If the landlord wins, the writ issues within five days."),
        ("Execution.", " The constable or deputy serves the writ and gives the occupants twenty-four hours to leave; after that the deputy may remove them. A tenant who appeals must post a bond within five days or the appeal does not stop the eviction."),
    ]) +
    f'<p>Uncontested cases take roughly three to five weeks from filing to the writ; contested cases take longer. Rent keeps accruing while the tenant stays, and a landlord who accepts rent after the rule is issued does not waive the eviction ({cite("ejectment", "S.C. Code § 27-37-150")}). Full detail is on the {A("south-carolina-eviction-process", "eviction process page")}.</p>'
    '<h2>Where these cases are heard</h2>'
    '<p>Dorchester County evictions for the Summerville area are filed at the Summerville magistrate’s office at the Troy Knight Judicial Complex on Deming Way, which has a dedicated evictions clerk; the St. George office covers the upper county. Berkeley County cases are heard in the county’s magistrate courts, and Charleston County’s in its civil magistrate court. All three counties post the Application for Ejectment and the Notice to Quit on their websites or use the statewide forms.</p>'
    '[[courts:dorchester_magistrate_summerville,dorchester_magistrate_stgeorge]]'
    '<h2>Why a former magistrate</h2>'
    f'<p>Evictions are decided by magistrates, in a courtroom where most landlords and tenants appear without a lawyer and most cases are won or lost on the paperwork. Tara Frost sat on that bench in Dorchester County for three years before returning to practice. She knows which notices the court looks for, what a magistrate will and will not accept as proof of service or of a lease violation, and how to present a tenant’s defense in the ten minutes the docket allows. She does not appear in matters she handled as a judge. Read {A("attorneys/tara-frost", "Tara’s background")}.</p>'
    '<h2>Fees</h2>'
    '<p>Uncontested evictions are handled for a flat fee quoted up front, plus the court’s filing and service costs. Contested evictions, tenant defense and deposit claims are quoted after we see the lease and the notices, and many are flat fees as well. Property managers and landlords with several units can arrange a standing rate.</p>'
    + callout(f"<b>Frost first:</b> before you change a lock, withhold a deposit, skip a rent payment or sign a surrender agreement, call. The Act punishes the wrong move on either side with triple or treble damages and attorney’s fees. {TEL}")
    + band("A rental problem in Dorchester, Berkeley or Charleston County?", "Call today. We will tell you what the Act requires, what the magistrate will expect, and what it will cost.")
)
page(HUB, kind="hub", section_label="Landlord-tenant services",
     title="Eviction and Landlord-Tenant Attorney in Summerville, SC | Frost Law Group",
     description="Evictions, tenant defense, security deposits and leases in the Dorchester, Berkeley and Charleston County magistrate courts, from a former Dorchester County magistrate judge. The South Carolina Residential Landlord and Tenant Act explained for both sides.",
     h1="Eviction and Landlord-Tenant Attorney in Summerville, SC", eyebrow="For landlords and tenants", nav_label="Landlord-tenant", hero_image="office-exterior.jpg", hero_caption="Frost Law Group, 128 Linwood Lane, Summerville",
     lead="Evictions, tenant defense, security deposits and leases under the South Carolina Residential Landlord and Tenant Act, handled by an attorney who presided over these cases as a Dorchester County magistrate.",
     summary="Evictions, tenant defense, security deposits and leases in the tri-county magistrate courts.",
     body=hub_body, priority=0.85,
     faqs=[
         ("How long does an eviction take in South Carolina?", "An uncontested eviction usually takes three to five weeks from the filing of the Application for Ejectment to the writ: service of the rule, the tenant’s ten days to respond, and issuance and execution of the writ with twenty-four hours’ notice. A contested case with a hearing, or a jury demand, takes longer."),
         ("Can a landlord evict a tenant without going to court in South Carolina?", "No. The only lawful way to remove a tenant is a Writ of Ejectment from the magistrate, executed by a constable or deputy. Changing locks, cutting utilities or removing belongings exposes the landlord to three months’ rent or twice the tenant’s actual damages, whichever is greater, plus attorney’s fees."),
         ("How much notice does a landlord have to give before evicting for nonpayment?", "Written notice and five days to pay, under § 27-40-710(B). A written lease that says in conspicuous language that nonpayment constitutes notice satisfies the requirement for the whole term, which is why most Lowcountry leases contain that clause and most nonpayment cases are filed on the sixth day."),
         ("Do I need a lawyer for an eviction in magistrate court?", "A landlord with a clean lease and a simple nonpayment case can often file without one. Hire a lawyer when the tenant has raised repair or retaliation defenses, when the ground is a lease violation rather than rent, when there is a dispute about who the tenant is, or when the amount at stake justifies getting it right the first time. Tenants with a real defense should not go in alone."),
         ("Do you represent tenants as well as landlords?", "Yes, in different cases. We represent tenants facing eviction, tenants whose deposits were withheld, and tenants whose landlords will not make repairs, and we represent landlords in evictions, deposit disputes and lease matters. We never represent both sides of the same dispute."),
     ])

# ----------------------------------------------------------------------------- SPOKES
sp("south-carolina-eviction-process", card_new=True,
   title="The South Carolina Eviction Process | Notices, the Rule to Vacate and the Writ, Step by Step",
   description="How eviction works in South Carolina under § 27-37-10 and the Residential Landlord and Tenant Act: the five-day and fourteen-day notices, the Application for Ejectment and $40 fee, the Rule to Vacate or Show Cause, the tenant’s ten days, the hearing, the writ and the twenty-four-hour execution.",
   h1="The South Carolina Eviction Process: Notices, the Rule to Vacate and the Writ, Step by Step", nav_label="SC eviction process",
   lead="South Carolina evictions move fast and follow a fixed script in magistrate court. Here is the script, with the deadlines on both sides, from a former magistrate.",
   summary="Grounds, notices, the Application for Ejectment, the ten-day rule, the hearing, the writ and the timeline.",
   body=(
       answer(f"In South Carolina a landlord evicts a tenant by filing an Application for Ejectment in the magistrate court for the county where the property is, after giving whatever notice the lease and the Residential Landlord and Tenant Act require. The magistrate issues a Rule to Vacate or Show Cause; the tenant has ten days after service to request a hearing; if the tenant does not, or loses at the hearing, the magistrate issues a Writ of Ejectment, and a constable or deputy gives the occupants twenty-four hours to leave ({cite('ejectment', 'S.C. Code § 27-37-10 et seq.')}). Uncontested cases take roughly three to five weeks from filing. The filing fee is $40 plus a small fee for the writ.", "The short answer")
       + '<h2>Step 1: a lawful ground</h2>'
       f'<p>{cite("ejectment", "S.C. Code § 27-37-10")} allows ejectment on three grounds: the tenant failed to pay rent when due or when demanded; the term of the tenancy has ended; or the tenant violated a term or condition of the lease. Everything else, including a landlord’s wish to renovate or move a relative in, has to fit one of those three, usually by ending a month-to-month tenancy with thirty days’ written notice.</p>'
       '<h2>Step 2: the notice the ground requires</h2>'
       + table(["Ground", "Notice required", "Statute"], [
           ["Nonpayment of rent", "Written notice and five days to pay. A written lease that states in conspicuous, bold type that nonpayment constitutes notice satisfies this for the entire term, so the landlord may file on the sixth day without a separate letter.", "§ 27-40-710(B); § 27-37-10(B)"],
           ["Other lease violation (unauthorized occupants, pets, damage, nuisance)", "Written notice specifying the violation and stating that the lease ends in fourteen days unless it is cured. If the tenant cures in time, no eviction.", "§ 27-40-710(A)"],
           ["Month-to-month tenancy", "Written notice at least thirty days before the termination date (seven days for week-to-week).", "§ 27-40-770"],
           ["End of a fixed-term lease (holdover)", "None beyond the lease itself; a tenant who stays past the end date is a holdover and may be ejected, and a willful holdover owes up to three months’ rent or double damages plus attorney’s fees.", "§ 27-40-770"],
       ]) +
       '<p>Most contested evictions turn on this step. A notice that names the wrong amount, the wrong date, the wrong cure period or the wrong tenant, or that was never delivered in a way the landlord can prove, is the tenant’s best defense and the landlord’s most expensive mistake.</p>'
       '<h2>Step 3: the Application for Ejectment</h2>'
       f'<p>The landlord, or an agent or attorney, files the Application for Ejectment in the magistrate court for the county where the property is: the Summerville magistrate’s office on Deming Way for most of the Summerville area, St. George for upper Dorchester County, the Berkeley County magistrate courts for Goose Creek, Moncks Corner and the Berkeley side of Summerville, and the Charleston County civil magistrate court for North Charleston, Charleston and Mount Pleasant. The filing fee is $40, with a small additional fee when the writ issues. The application states the ground, the amount of rent owed if any, and the names of the tenants; adults who are not named are not covered by the writ, so landlords should name every adult occupant they know of. Back rent and damages up to the magistrate’s {cite("magistrate_civil", "$7,500 civil limit")} can be claimed in the same case.</p>'
       '<h2>Step 4: the Rule to Vacate or Show Cause and the tenant’s ten days</h2>'
       f'<p>The magistrate issues a written rule requiring the tenant to vacate or to show cause, within ten days after service, why they should not be ejected. A constable or deputy serves it. Those ten days are the tenant’s window: a written request for a hearing, filed with the magistrate, stops the writ and sets the case for trial. A tenant who does nothing is ejected on the eleventh day without a hearing ({cite("ejectment", "S.C. Code § 27-37-40")}). Paying the rent after the rule is issued does not end the case unless the landlord agrees; the statute says the landlord’s acceptance of rent after the rule does not waive the right to ejectment, and rent keeps accruing while the tenant stays.</p>'
       '<h2>Step 5: the hearing</h2>'
       '<p>Hearings are short and usually set within a few weeks. The landlord goes first and must prove the lease, the ground and the notice; the tenant answers. Either side may demand a jury trial, which lengthens the case. Common tenant defenses: the notice was defective or never given; the rent was tendered before the case was filed and refused; the landlord failed to repair a health or safety condition after written notice under § 27-40-610; the eviction is retaliation for a complaint to a housing or code agency, a complaint to the landlord about repairs, or joining a tenants’ organization (§ 27-40-910); the case names the wrong person or the wrong unit; or the lease has not ended. Counterclaims for a withheld deposit or for repair costs can be raised in the same case.</p>'
       '<h2>Step 6: the writ and the twenty-four hours</h2>'
       f'<p>If the tenant does not request a hearing, or the magistrate rules for the landlord, the magistrate issues a Writ of Ejectment, within five days of a verdict for the landlord. Under {cite("ejectment", "S.C. Code § 27-37-160")} the constable or deputy goes to the property, presents the writ and gives the occupants twenty-four hours to leave voluntarily. If they do not, or the premises appear unoccupied, a deputy sheriff (not a constable) may enter by force using the least destructive means. A writ posted on the door when no one answers works the same way after twenty-four hours.</p>'
       '<h2>Appeals</h2>'
       '<p>A tenant may appeal to the circuit court, but the appeal does not stop the eviction unless the tenant posts an appeal bond, in an amount the magistrate sets, within five days of serving the notice of appeal (§ 27-37-130). In practice very few tenants can, which is why the hearing is the place to win.</p>'
       '<h2>The timeline in a typical nonpayment case</h2>'
       + table(["Day", "What happens"], [
           ["Day 1", "Rent is due and unpaid."],
           ["Day 6", "The five-day period has run; if the lease contains the conspicuous nonpayment clause, the landlord may file."],
           ["Days 6–8", "Application for Ejectment filed; the magistrate issues the Rule to Vacate or Show Cause."],
           ["Days 8–14", "The constable or deputy serves the rule."],
           ["Service + 10 days", "The tenant’s deadline to request a hearing."],
           ["Day 20–25 (no hearing requested)", "Writ of Ejectment issues; the deputy serves it and gives twenty-four hours."],
           ["Weeks 4–8 (hearing requested)", "Hearing held; if the landlord prevails, the writ issues within five days and is executed."],
       ]) +
       '<h2>What landlords get wrong</h2>'
       + checks(["Filing on the wrong ground, or filing for nonpayment when the lease has no notice clause and no letter was sent",
                 "Accepting partial rent with a side promise and then losing track of what was agreed",
                 "Leaving an adult occupant off the application, so the writ does not cover them",
                 "Any form of self-help: a changed lock, a cut utility, a removed door, a text that says “be out by Friday or I’ll put your things on the curb”",
                 "Disposing of belongings left behind without following the Act’s abandonment procedure"]) +
       '<h2>What tenants get wrong</h2>'
       + checks(["Ignoring the rule because the rent is almost together; the ten days do not wait",
                 "Requesting the hearing orally, by text to the landlord, or anywhere but with the magistrate",
                 "Withholding rent for repairs without the written fourteen-day notice the Act requires",
                 "Moving out without a written surrender and a forwarding address, then losing the deposit claim",
                 "Appealing without the bond and expecting the eviction to stop"])
       + callout("<b>Frost first:</b> whichever side you are on, the paperwork decides the case. A landlord should have us read the lease and the notice before filing; a tenant should call the day the rule is served, not the day before the hearing.")
       + band("Need an eviction filed, or defended, in Dorchester, Berkeley or Charleston County?", "Call. We will tell you what the magistrate will look for and what it will cost.")
   ),
   faqs=[
       ("How long does it take to evict a tenant in South Carolina?", "About three to five weeks from filing in an uncontested nonpayment case: service of the rule, the tenant’s ten days, and the writ with twenty-four hours’ notice. A hearing or a jury demand adds weeks."),
       ("How much does it cost to file an eviction in South Carolina?", "The magistrate court filing fee for an Application for Ejectment is $40, plus a small fee when the writ issues and the constable’s service costs. Attorney’s fees are separate; uncontested cases are usually a flat fee."),
       ("What is a Rule to Vacate or Show Cause?", "The magistrate’s order, served on the tenant after the landlord files, requiring the tenant to leave or to show cause within ten days why they should not be ejected. Requesting a hearing within those ten days is how a tenant shows cause."),
       ("Can a landlord evict in South Carolina without a lease?", "Yes. A tenant without a written lease is usually a month-to-month tenant, and the landlord can end the tenancy with thirty days’ written notice or file for nonpayment after written notice and five days."),
       ("Can a tenant stop an eviction by paying the rent?", "Only if the landlord agrees or the payment was tendered before the case was filed. Once the rule is issued, the statute says accepting rent does not waive the landlord’s right to ejectment, though many landlords will dismiss on full payment."),
       ("What happens to belongings left behind after an eviction?", "The Act has a procedure for property a tenant abandons, and the writ allows the deputy to set belongings out. Landlords should document everything and follow the Act rather than disposing of property immediately; tenants should take what matters before the deputy arrives."),
   ],
   related=["south-carolina-security-deposit-law", "bond-hearings", "traffic-tickets"])

sp("south-carolina-security-deposit-law", card_new=True,
   title="South Carolina Security Deposit Law | The 30-Day Rule, Deductions and Triple Damages",
   description="What South Carolina law says about security deposits under § 27-40-410: the thirty-day return rule, the itemized statement, what a landlord may deduct, normal wear and tear, the three-times penalty for wrongful withholding, and how to make the demand and sue in magistrate court.",
   h1="South Carolina Security Deposit Law: The 30-Day Rule, Deductions and Triple Damages", nav_label="SC security deposit law",
   lead="South Carolina does not cap security deposits, but it is strict about giving them back. Here is the thirty-day rule, what can be deducted, and what a landlord who gets it wrong owes.",
   summary="The thirty-day return rule, the itemized statement, lawful deductions, the three-times penalty and how to enforce it.",
   body=(
       answer(f"Under {cite('rlta', 'S.C. Code § 27-40-410')}, a landlord must return a tenant’s security deposit, less any amounts withheld for unpaid rent and for damage beyond normal wear and tear, within thirty days after the tenancy ends, the tenant delivers possession and the tenant demands it. Any deduction must be itemized in a written statement. A landlord who fails to comply owes the tenant the amount wrongfully withheld, an additional amount equal to three times that figure, and reasonable attorney’s fees. There is no statutory limit on the size of a deposit in South Carolina. Claims are brought in magistrate court, which hears civil cases up to $7,500.", "The short answer")
       + '<h2>What the statute requires of a landlord</h2>'
       + checks(["<b>Return within thirty days.</b> The clock starts when all three things have happened: the tenancy has ended, the tenant has delivered possession (keys back, belongings out), and the tenant has demanded the deposit. A written demand with a forwarding address starts the clock cleanly.",
                 "<b>Itemize every deduction.</b> A written statement listing each amount withheld and what it is for, sent with whatever balance is due.",
                 "<b>Deduct only what the Act allows.</b> Accrued rent, and damages the landlord suffered because the tenant failed to keep the unit as the Act requires: clean, undamaged, free of nuisance. Normal wear and tear is not damage.",
                 "<b>Use consistent standards.</b> A landlord with more than four adjoining units who applies different deposit standards to different tenants must post or disclose the standards; otherwise the same rules apply to everyone."]) +
       '<h2>What can be deducted, and what cannot</h2>'
       + table(["Usually a lawful deduction", "Usually not"], [
           ["Unpaid rent, including rent through the end of a lease the tenant broke, until the unit is re-rented", "Rent for months after the landlord re-rented the unit"],
           ["Holes in walls, broken fixtures, pet damage, stains that require replacing carpet", "Nail holes from pictures, minor scuffs, carpet worn by ordinary use, faded paint"],
           ["Cleaning needed because the unit was left dirty", "Routine cleaning and repainting the landlord would do between any tenants"],
           ["Unpaid utilities or fees the lease makes the tenant’s responsibility", "Charges the lease never mentioned, or “administrative” fees invented at move-out"],
           ["Replacing keys or remotes not returned", "Upgrades and improvements the landlord wanted anyway"],
       ]) +
       '<h2>The penalty: three times the amount wrongfully withheld</h2>'
       '<p>Section 27-40-410(b) is one of the sharpest teeth in the Act. If the landlord fails to return the deposit and the itemized statement as the statute requires, the tenant may recover the property and money due, an amount equal to three times the amount wrongfully withheld, and reasonable attorney’s fees. A $1,500 deposit kept without an itemization can become a judgment for $6,000 plus fees. Magistrates apply the statute as written, and a landlord’s explanation that “the tenant never gave me an address” carries little weight when the tenant can show a written demand.</p>'
       '<h2>How a tenant enforces it</h2>'
       + steps([
           ("Document the move-out.", " Photographs or video of every room on the day you leave, the keys handed over, and a copy of the lease and the move-in inspection if there was one."),
           ("Make the demand in writing.", " A dated letter or e-mail stating that you have vacated and returned the keys, demanding the deposit, and giving a forwarding address. Keep a copy. This starts the thirty days."),
           ("Wait thirty days.", " If the deposit, or an itemized statement with the balance, does not arrive, the statute has been violated."),
           ("Send a final demand citing § 27-40-410.", " Many landlords pay at this point. State the amount, the three-times penalty and the attorney’s fees exposure."),
           ("File in magistrate court.", " A small-claims complaint in the magistrate court for the county where the property is, within the court’s $7,500 limit. The hearing is informal, and your photographs and the demand letter are the case."),
       ]) +
       '<h2>How a landlord avoids the penalty</h2>'
       + checks(["Inspect at move-in with the tenant and keep a signed condition report with photographs",
                 "Inspect at move-out the day possession is delivered, and photograph everything",
                 "Send the itemized statement and any balance within thirty days to the forwarding address, or to the last known address if none was given, and keep proof of mailing",
                 "Charge actual costs with receipts, prorated for the age of carpet and paint, not round numbers",
                 "Put deposit terms, fees and the tenant’s cleaning obligations in the lease in plain words"]) +
       '<h2>Related rules tenants ask about</h2>'
       + checks(["<b>Pet deposits and nonrefundable fees.</b> The Act does not separately regulate them; what the lease says controls, and anything called a deposit is subject to the thirty-day rule.",
                 "<b>Last month’s rent.</b> A deposit is not last month’s rent unless the lease says so. Skipping the final payment and telling the landlord to keep the deposit is a nonpayment and a bad start to a deposit claim.",
                 "<b>Interest.</b> South Carolina does not require landlords to pay interest on deposits.",
                 "<b>A sold or foreclosed building.</b> The deposit obligation follows the property to the new owner; the tenant should demand it from whoever is the landlord at move-out."])
       + callout("<b>Frost first:</b> a landlord about to keep a deposit, or a tenant about to sue over one, should spend ten minutes on the phone with us first. The statute rewards the side that followed the procedure and punishes the one that did not, regardless of who was right about the carpet.")
       + band("A deposit dispute in Dorchester, Berkeley or Charleston County?", "Call. Many deposit claims resolve with one letter; the rest are decided in an afternoon in magistrate court.")
   ),
   faqs=[
       ("How long does a landlord have to return a security deposit in South Carolina?", "Thirty days after the tenancy ends, the tenant delivers possession and the tenant demands the deposit, under § 27-40-410. Any deductions must be itemized in writing."),
       ("Is there a limit on security deposits in South Carolina?", "No. The Act sets no maximum. Lowcountry landlords commonly ask for one month’s rent, sometimes more for pets or weak credit."),
       ("What can a landlord deduct from a security deposit in SC?", "Unpaid rent and damage beyond normal wear and tear that resulted from the tenant’s failure to keep the unit as the Act requires, plus charges the lease makes the tenant’s responsibility. Routine cleaning, repainting and ordinary wear cannot be charged."),
       ("What is the penalty for not returning a security deposit in South Carolina?", "The tenant may recover the amount wrongfully withheld, an additional three times that amount, and reasonable attorney’s fees."),
       ("What if I never gave my landlord a forwarding address?", "The thirty days start when you demand the deposit, so make the demand in writing with an address now. A landlord who was never asked has a defense; a landlord who was asked and did not itemize does not."),
       ("Where do I sue for my deposit?", "Magistrate court in the county where the rental is, as a small claim up to $7,500. The filing fee is modest, lawyers are not required, and hearings are usually set within a couple of months."),
   ],
   related=["south-carolina-eviction-process", "estate-planning-for-business-owners", "contact-us"])
