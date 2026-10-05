"""Probate hub and spokes."""
from .base import page, A, ext, img, p, ul, checks, steps, callout, answer, band, esc, table
from . import firm
from .local import cite, link

HUB = "probate"
TEL = f'<a href="tel:{firm.PHONE_E164}">{firm.PHONE}</a>'


def sp(slug, **kw):
    kw.setdefault("kind", "spoke")
    kw.setdefault("hub", HUB)
    kw.setdefault("eyebrow", "Probate · Summerville, SC")
    return page(slug, **kw)


hub_body = (
    answer("Frost Law Group handles probate and estate administration in the Dorchester, Berkeley and Charleston County probate courts—opening the estate, guiding the personal representative, dealing with creditors, and distributing and closing. Tara L. Frost served as a Dorchester County Associate Probate Judge from 2025 to 2026.", "Who helps with probate and estate administration in Summerville, SC?")
    + '<h2>What probate is</h2>'
    '<p>Probate is the court-supervised process of settling a person\'s affairs after death: proving the will (if there is one), appointing a personal representative, paying valid debts and taxes, and distributing what remains to the heirs or beneficiaries. In South Carolina it happens in the probate court of the county where the person lived—Dorchester County for Summerville, Berkeley County for Goose Creek and Moncks Corner, Charleston County for North Charleston, Charleston and Mount Pleasant.</p>'
    '<p>Not every estate needs full probate. The size of the estate, how assets are titled, and whether a valid will exists all change the path. We evaluate each family\'s situation and recommend the simplest route that works.</p>'
    '<h2>How we help</h2>'
    '[[cards:probate-process,executor-duties,small-estate-affidavit,probate-courts]]'
    '<h2>When there is a dispute</h2>'
    '<p>Probate is not always smooth. When heirs disagree, a personal representative will not account, or a will looks wrong, the probate court decides—and the family needs an attorney who knows how those hearings run.</p>'
    '[[cards:executor-disputes,will-contests,guardianship-and-conservatorship,trust-administration]]'
    '<h2>The South Carolina probate timeline, briefly</h2>'
    + steps([
        ("Deliver the will and open the estate.", f" Whoever holds the original will must deliver it to the probate court promptly after death ({cite('will_delivery', 'S.C. Code § 62-2-901')}). The court appoints the personal representative and issues letters (certificates of appointment)."),
        ("Notice to creditors.", f" A notice is published; creditors have eight months from first publication to file claims ({cite('creditor_period', 'S.C. Code § 62-3-801')}). This is why no South Carolina estate closes in less than eight months."),
        ("Inventory and appraisement.", " The personal representative files an inventory of the estate's assets and values within the time the court sets."),
        ("Pay debts, taxes and expenses.", " Valid claims are paid in the statutory order; final income tax returns are filed."),
        ("Distribute and close.", " Assets go to beneficiaries, receipts are collected, and a final accounting or application for settlement closes the estate."),
    ]) +
    '<h2>Assets that go through probate—and those that do not</h2>'
    + table(["Goes through probate", "Passes outside probate"], [
        ["Property titled solely in the decedent's name", "Assets in a properly funded revocable living trust"],
        ["Real estate owned individually, with no survivorship or transfer-on-death deed", "Jointly owned property with right of survivorship"],
        ["Bank and investment accounts with no beneficiary designation", "Life insurance and retirement accounts with a named living beneficiary"],
        ["Vehicles, jewelry and household goods with no surviving joint owner", "Accounts with payable-on-death or transfer-on-death designations"],
    ]) +
    f'<p>Planning ahead can keep most of an estate out of court. {A("revocable-trust", "Revocable trusts")}, beneficiary designations and transfer-on-death provisions let assets pass directly to your family. Ask us how to build a plan that works.</p>'
    '<h2>Why families in Summerville choose us for probate</h2>'
    + checks(["Tara Frost sat as an Associate Probate Judge in Dorchester County and as a Magistrate Judge before that; she knows what the court needs to see and what slows a file down.",
              "We tell you when you do not need us—small estates and simple affidavits included.",
              "Flat fees for uncontested estates where the facts allow it, quoted in writing.",
              "One office for probate, guardianship and estate planning, so the estate we close can end with a plan for the survivors."]) +
    band("We are here to help your family.", "Probate can feel overwhelming after a loss. Call and we will tell you what the court will need and what you can do yourself.")
)
page(HUB, kind="hub", section_label="Probate services",
     title="Probate Attorney in Summerville, SC | Dorchester, Berkeley & Charleston County Estates",
     description="Summerville, SC probate attorney Tara Frost, a former Dorchester County Associate Probate Judge, guides families through estate administration, executor duties, small estates, will contests and guardianship.",
     h1="Probate Attorney in Summerville, SC", eyebrow="Guiding families through the probate process", nav_label="Probate", hero_image="hero-probate.jpg", hero_caption="Probate court",
     lead="Losing a loved one is hard enough. Let Frost Law Group handle the legal process so your family can focus on what matters most.",
     summary="Estate administration, executor guidance, small estates, disputes and guardianship.",
     body=hub_body, priority=0.9,
     faqs=[
         ("How long does probate take in South Carolina?", "Eight months to a year for a typical uncontested estate, because creditors have eight months to file claims. Contested estates, real estate sales and tax issues take longer."),
         ("Do I need a lawyer to probate an estate?", f"Not always. Small estates and simple ones with cooperative heirs can often be handled by the personal representative with the court's forms. We will tell you which yours is. See {A('small-estate-affidavit', 'small estate affidavits')}."),
         ("What does a probate attorney cost?", "For uncontested estates we usually quote a flat fee once we see the assets and the will; contested matters are billed hourly with a written estimate. Fees are paid from the estate, not by the personal representative personally."),
     ])

sp("probate-process",
   title="The South Carolina Probate Process, Step by Step | Summerville Probate Attorneys",
   description="What happens from the day of death to the day the estate closes in a South Carolina probate court: delivering the will, appointment, creditor notice, inventory, taxes, distribution and closing. Summerville attorneys explain.",
   h1="The South Carolina Probate Process, Step by Step", nav_label="The probate process",
   lead="What actually happens, in order, from the first week after a death to the day the court closes the estate.",
   summary="Every step from delivering the will to closing the estate, with the deadlines that matter.",
   body=(
       '<h2>The first two weeks</h2>'
       f'<p>Locate the original will and deliver it to the probate court of the county where the person lived; South Carolina requires whoever holds it to do so ({cite("will_delivery", "S.C. Code § 62-2-901")}). Order several certified death certificates. Secure the home and vehicles, forward mail, and do not distribute anything—not even personal items—until the personal representative is appointed. Nothing else is urgent.</p>'
       '<h2>Step by step</h2>'
       + steps([
           ("Application or petition.", " The person named in the will (or, with no will, the person with statutory priority—usually the spouse or an heir) applies to the probate court to be appointed. Most estates open informally, without a hearing; a formal petition is used when a will is questioned or heirs disagree."),
           ("Appointment and letters.", " The court issues letters testamentary or letters of administration—the document banks, the DMV and title companies will ask for. A bond may be required unless the will waives it or the heirs consent."),
           ("Notice to creditors.", f" The court publishes notice; creditors have eight months from first publication to present claims ({cite('creditor_period', 'S.C. Code § 62-3-801')}). Known creditors should be notified directly."),
           ("Inventory and appraisement.", " A sworn list of the estate's assets and their date-of-death values, filed with the court on its form. Real estate, vehicles, accounts, business interests and personal property are all included; appraisals are used where values are not obvious."),
           ("Managing the estate.", " Open an estate bank account under a new tax ID, collect assets, keep insurance in force, and keep every receipt. The personal representative acts as a fiduciary and can be held personally responsible for losses."),
           ("Claims, debts and taxes.", " Allow or deny each claim in writing. Pay valid debts in the statutory order of priority. File the decedent's final income tax return and, if the estate earns income, a fiduciary return."),
           ("Distribution.", " After the creditor period closes and debts are paid, distribute according to the will or intestacy statute and collect signed receipts from each beneficiary. Real estate passes by deed of distribution."),
           ("Closing.", " File the final accounting (or an application for settlement with waivers from the beneficiaries). The court approves it and discharges the personal representative."),
       ]) +
       '<h2>How long it takes</h2>'
       '<p>Because of the creditor period, the fastest an ordinary South Carolina estate closes is a little over eight months. Ten to fourteen months is common. Real estate that must be sold, a business, an out-of-state asset, a tax audit or a family disagreement can stretch it to two years or more.</p>'
       '<h2>What can go wrong</h2>'
       + checks(["Distributing early and running out of money for a late creditor claim—the personal representative pays it personally",
                 "Missing the inventory deadline or filing values that cannot be supported",
                 "Commingling estate money with personal accounts",
                 "Selling real estate without the authority the will or court gives",
                 "Letting a beneficiary take the truck and the tools before the accounting"]) +
       f'<p>Most of these are avoidable with a checklist and a phone call. Our {A("executor-duties", "guide for personal representatives")} goes deeper.</p>'
       + band("Need a hand with an estate?", "Bring the will and a list of assets. We will map the process and tell you which steps you can do yourself.")
   ),
   faqs=[
       ("What is the difference between informal and formal probate?", "Informal probate is handled by the court's staff without a hearing and works when the will is clear and nobody objects. Formal probate is a court proceeding with notice and a judge's order, used when there is a dispute or a defect to resolve."),
       ("Can the personal representative be paid?", "Yes. South Carolina allows a reasonable commission, generally up to five percent of the personal property received, and reimbursement of expenses."),
   ],
   related=["executor-duties", "small-estate-affidavit", "probate-courts"])

sp("executor-duties",
   title="Executor (Personal Representative) Duties in South Carolina | Summerville Probate Attorney",
   description="What a South Carolina personal representative must do, in what order, with which deadlines—and the mistakes that create personal liability. Guidance from a former Dorchester County probate judge.",
   h1="Executor and Personal Representative Duties in South Carolina", nav_label="Executor duties",
   lead="You were named in the will, or the family chose you. Here is what the job actually involves, and where people get into trouble.",
   summary="The personal representative's checklist, deadlines and liabilities.",
   body=(
       answer("A South Carolina personal representative (executor) must deliver the will, get appointed, notify creditors, inventory and safeguard the assets, pay valid debts and taxes in the right order, distribute to the right people, account to the court, and act loyally and prudently throughout. Frost Law Group advises personal representatives in the Dorchester, Berkeley and Charleston County probate courts on every step.", "What does an executor of a will do in Summerville, SC?")
       + '<h2>The job, in order</h2>'
       + steps([
           ("Get appointed before you act.", " Until the court issues letters, you have no authority. Do not close accounts, sell anything or promise distributions."),
           ("Protect the assets.", " Change locks if needed, keep homeowner's and auto insurance in force, secure valuables, and collect mail. Photograph the contents of the home before family members remove anything."),
           ("Open an estate account.", " Get an EIN for the estate, open a checking account in the estate's name, and run every dollar through it. Never mix estate money with your own."),
           ("Notify and communicate.", " Creditors, the Social Security Administration, pension plans, insurers, and the beneficiaries. Beneficiaries are entitled to information; silence causes disputes."),
           ("Inventory.", " List every asset with a date-of-death value and file it on the court's form. Get appraisals for real estate, vehicles and collections."),
           ("Handle claims.", f" Review each claim, allow or disallow it in writing, and pay allowed claims in statutory priority after the creditor period ({cite('creditor_period', 'S.C. Code § 62-3-801')}). Funeral expenses, administration costs and taxes come before general creditors."),
           ("Taxes.", " File the decedent's final Form 1040 and SC1040, a fiduciary return if the estate earns income, and property taxes on real estate the estate holds."),
           ("Distribute and account.", " Distribute per the will or statute, get signed receipts, and file the accounting the court requires to close."),
       ]) +
       '<h2>Standards you are held to</h2>'
       '<p>A personal representative is a fiduciary: you must act in the beneficiaries\' interest, not your own, with the care a prudent person uses with their own affairs. You cannot buy estate property for yourself without court approval or beneficiary consent, favor one beneficiary, or use estate funds for personal expenses. Breaches lead to surcharge—paying the loss from your own pocket—and removal.</p>'
       '<h2>Compensation</h2>'
       '<p>South Carolina allows a reasonable commission, generally up to five percent of the personal property the estate receives (real estate is treated differently), plus reimbursement of legitimate expenses. Many family members waive it; the choice is yours, and it should be documented.</p>'
       '<h2>When you should call a lawyer</h2>'
       + checks(["The estate includes real estate to sell, a business, or out-of-state property", "A creditor claim looks wrong or large", "A beneficiary is unhappy, unreachable, a minor, or receiving benefits", "The will is unclear, was changed late in life, or is being questioned", "You are unsure whether an asset is a probate asset at all"]) +
       f'<p>If a dispute has already started, see {A("executor-disputes", "executor and beneficiary disputes")}.</p>'
       + band("Named as executor?", "We will walk you through the appointment and give you the checklist, whether or not you hire us for the rest.")
   ),
   faqs=[
       ("Can I be removed as personal representative?", "Yes, by the court, for mismanagement, conflict of interest, failure to account or failure to act. Beneficiaries petition; a hearing follows."),
       ("Do I have to serve if I was named?", "No. You can decline, and the alternate named in the will (or the next person with priority) is appointed instead."),
       ("Am I personally liable for the decedent's debts?", "Not for the debts themselves—only for losses you cause by mishandling the estate, such as distributing before paying a valid claim."),
   ],
   related=["probate-process", "executor-disputes", "probate-courts"])

sp("executor-disputes", card_new=True,
   title="Executor Disputes in Summerville, SC Probate Court | Frost Law Group",
   description="Who handles executor disputes in Summerville, SC probate court: removal petitions, demands for an accounting, self-dealing claims and contested distributions in Dorchester, Berkeley and Charleston counties. Former probate judge.",
   h1="Executor and Beneficiary Disputes in Summerville, SC Probate Court", nav_label="Executor disputes",
   lead="When the person running the estate is not doing the job—or is accused of it—the probate court decides. We represent both sides.",
   summary="Removal petitions, accountings, self-dealing and contested distributions.",
   body=(
       answer("Frost Law Group represents beneficiaries who believe an estate is being mishandled and personal representatives who are accused of it, in the Dorchester, Berkeley and Charleston County probate courts. Tara L. Frost served as a Dorchester County Associate Probate Judge and knows how these hearings are decided.", "Who handles executor disputes in Summerville, SC probate court?")
       + '<h2>Disputes we see most often</h2>'
       + checks(["<b>No information.</b> The personal representative will not share the inventory, the accounting or the will. Beneficiaries have a right to reasonable information and can petition the court to compel it.",
                 "<b>Delay.</b> The estate has been open for years with no accounting and no distribution.",
                 "<b>Self-dealing.</b> The personal representative bought the house cheaply, sold the truck to a cousin, or paid themselves fees nobody agreed to.",
                 "<b>Missing assets.</b> Accounts emptied before or after death, often under a power of attorney that should have ended at death.",
                 "<b>Unequal treatment.</b> One sibling's loan forgiven, another's counted; the house given to the child who lived in it.",
                 "<b>A questionable will.</b> If the dispute is really about whether the will is valid, see " + A("will-contests", "will contests") + "."]) +
       '<h2>What the probate court can do</h2>'
       '<p>Order an accounting; surcharge the personal representative for losses; remove and replace them; void improper sales; require a bond; award attorney\'s fees against a fiduciary who acted in bad faith; and, where property is being dissipated, act quickly on a motion. Most disputes settle once a judge orders the numbers onto the table.</p>'
       '<h2>If you are the personal representative</h2>'
       '<p>Being accused is not the same as being wrong. Beneficiaries frequently misunderstand why an estate stays open for eight months, why real estate cannot be given away before debts are paid, or why a commission is allowed. Good records and a prompt, complete accounting end most complaints. We help personal representatives prepare the accounting and respond to a petition without escalating the family fight.</p>'
       '<h2>Timing</h2>'
       '<p>Objections to an accounting or a proposed distribution must be raised before the court approves them; once an estate is closed, reopening it is harder and sometimes impossible. If you have received a notice of a proposed settlement, call before the date on it.</p>'
       + band("Estate not being handled right?", "Bring what you have—notices, the will, bank statements. We will tell you whether the court can help and what it will cost to find out.")
   ),
   faqs=[
       ("Can a beneficiary demand an accounting in South Carolina?", "Yes. Beneficiaries can request information informally and petition the probate court to compel a formal accounting if it is refused."),
       ("How do I remove an executor in South Carolina?", "File a petition for removal in the probate court stating the grounds—mismanagement, conflict of interest, failure to account or failure to act—and the court holds a hearing."),
       ("Does the estate pay my attorney's fees?", "Sometimes. The court can award fees from the estate when the action benefited the estate, and against a fiduciary who acted in bad faith. Ask us to assess your case."),
   ],
   related=["executor-duties", "will-contests", "trust-administration"])

sp("small-estate-affidavit",
   title="Small Estate Affidavit in South Carolina | The $45,000 Limit, Form 420ES and Fees",
   description="When a South Carolina estate can skip full probate: the $45,000 small-estate affidavit under § 62-3-1201 (raised from $25,000 in 2025), Form 420ES, what counts toward the limit, the filing fee, and how to file in Dorchester, Berkeley or Charleston County.",
   h1="Small Estate Affidavit in South Carolina: The $45,000 Limit, the Form and the Fee", nav_label="Small estates",
   lead="Not every estate needs eight months of probate. Here is when a South Carolina family can collect a small estate with an affidavit instead, what it costs, and when the affidavit is the wrong tool. The limit rose from $25,000 to $45,000 on May 8, 2025.",
   summary="The $45,000 affidavit (Form 420ES), the fee, what counts toward the limit and the summary procedure for small estates.",
   body=(
       answer(f"If the entire probate estate, meaning everything passing under the will or by intestacy, less liens, is worth $45,000 or less and at least thirty days have passed since the death, a successor can collect the decedent’s personal property with an affidavit under {cite('small_estate', 'S.C. Code § 62-3-1201')} instead of opening a full estate. The affidavit is Form 420ES, it must be approved and countersigned by the probate judge of the county where the decedent lived, and the filing fee follows the estate fee schedule: $25 for property under $5,000, $45 up to $20,000 and $67.50 up to $45,000. The affidavit transfers personal property only; real estate still needs an estate. Act 26 of 2025 raised the ceiling from $25,000 to $45,000 effective May 8, 2025.", "The short answer")
       + '<h2>Who qualifies</h2>'
       + checks(["A total probate estate of $45,000 or less after subtracting liens: bank accounts, vehicles, final paychecks, refunds, household goods, anything passing under the will or by intestacy, wherever located",
                 "At least thirty days since the death",
                 "No personal representative appointed and no application pending, here or anywhere else",
                 "The person signing is a successor entitled to the property: an heir under the will or the intestacy statute, or someone who paid reasonable funeral expenses, who counts as a claiming successor under the statute",
                 "Personal property only; real estate titled solely in the decedent’s name cannot pass by affidavit"]) +
       '<h2>What does not count toward the $45,000</h2>'
       '<p>Assets that pass outside probate are not part of the calculation: life insurance and retirement accounts with named beneficiaries, jointly owned accounts and real estate with survivorship, payable-on-death and transfer-on-death accounts, and anything already in a trust. A family with a $350,000 house held jointly, a $200,000 IRA with a named beneficiary and a $30,000 checking account in Dad’s name alone can usually use the affidavit for the checking account.</p>'
       '<h2>How to file, step by step</h2>'
       + steps([("Gather the numbers.", " Statements as of the date of death, vehicle titles and a certified death certificate. Value vehicles at fair market value and subtract any loan balance."),
                ("Complete Form 420ES.", f" The Affidavit for Collection of Personal Property Pursuant to Small Estate Proceedings is a statewide form published by the {link('sccourts_probate_forms', 'South Carolina Judicial Branch')}. It lists the property, the value, the heirs and their shares, and it is signed under oath."),
                ("File it with the original will, if any.", f" The will must be delivered to the probate court within thirty days of death in any event ({cite('will_delivery', 'S.C. Code § 62-2-901')}). The court checks that no estate has been opened and that thirty days have passed."),
                ("The judge approves and countersigns.", " The clerk reviews the affidavit, the judge signs it, and the court issues certified copies, usually within a few days to two weeks depending on the county."),
                ("Present it.", " A certified copy is presented to the bank, the DMV, the employer or the brokerage, which is protected by statute when it releases the property to the affiant."),
                ("Distribute honestly.", " The affiant holds what is collected for the heirs and remains answerable to them and to creditors for it.")]) +
       '<h2>What it costs in Dorchester, Berkeley and Charleston County</h2>'
       f'<p>The affidavit fee is the estate filing fee in {cite("probate_fees", "S.C. Code § 8-21-770")} based on the value listed, and it is the same in every county:</p>'
       + table(["Value of the property collected", "Fee"], [["Under $5,000", "$25"], ["$5,000 to $19,999", "$45"], ["$20,000 to $45,000", "$67.50"]]) +
       f'<p>Certified copies are $5 each, and you will want one for each institution. Each county court has its own intake routine: the {A("dorchester-county-probate-court", "Dorchester County Probate Court")} in St. George asks people filing without a lawyer to complete its Opening Probate Worksheet first; the {A("berkeley-county-probate-court", "Berkeley County Probate Court")} in Moncks Corner takes walk-ins in the morning and has a drop box; the {A("charleston-county-probate-court", "Charleston County Probate Court")} accepts filings through EZ-Filing and by appointment.</p>'
       '<h2>Summary administration: the other small-estate route</h2>'
       '<p>When the estate is slightly too large for the affidavit, or when real estate is involved, a personal representative is appointed but the estate can often be closed quickly. Under § 62-3-1203 an estate that does not exceed $45,000, or that does not exceed exempt property, family allowances, costs of administration, funeral expenses and medical expenses of the last illness, can be distributed immediately and closed with a verified closing statement after notice to creditors is published. The eight-month creditor period still runs, but the paperwork is a fraction of a regular estate.</p>'
       '<h2>When an affidavit is the wrong tool</h2>'
       '<p>Real estate in the decedent’s name alone, a vehicle with a loan larger than its value, a lawsuit or injury claim to pursue, a dispute among the heirs, or creditors who will not be paid in full all call for a regular estate. Filing an affidavit for an estate that needed probate creates personal liability to creditors and heirs, and the bank will not tell you whether an affidavit is correct; it will simply accept or reject it.</p>'
       + callout(f"<b>Frost first:</b> a ten-minute call sorts out whether your family qualifies. If an affidavit will do, we will say so, and we can prepare it for a flat fee or point you to the form. {TEL}")
       + band("Is your family’s estate small enough?", "Tell us what was owned and how it was titled. If an affidavit will do, we will say so.")
   ),
   faqs=[
       ("What is the small estate limit in South Carolina?", "$45,000, measured by the probate estate less liens. The limit was $25,000 until Act 26 of 2025 raised it, effective May 8, 2025."),
       ("Can I use a small estate affidavit for a house?", "No. Real estate in the decedent’s name passes through a regular probate estate, even when the rest of the estate is small. Summary administration may still shorten that estate."),
       ("How long does a small estate affidavit take in South Carolina?", "You must wait thirty days after the death to file. Once filed, the court’s review and the judge’s signature commonly take a few days to two weeks, and institutions usually release funds within a week or two of receiving the certified affidavit."),
       ("Do I need a lawyer for a small estate affidavit?", "Not always. Families with one or two accounts and heirs who agree often file it themselves. Call us when there is a will that does not match the intestacy shares, a vehicle with a lien, a creditor problem, or any doubt about whether the estate is under $45,000."),
       ("Does the thirty-day waiting period start at death or at filing the will?", "At death. The will still must be delivered to the probate court within thirty days of death under § 62-2-901."),
   ],
   related=["probate-process", "executor-duties", "probate-courts"])

sp("will-contests", card_new=True,
   title="Will Contests & Probate Litigation in Summerville, SC | Frost Law Group",
   description="Grounds to contest a will in South Carolina—lack of capacity, undue influence, fraud and improper execution—who can bring one, the deadlines, and how the probate court decides. Summerville probate litigation attorneys.",
   h1="Will Contests and Probate Litigation in Summerville, SC", nav_label="Will contests",
   lead="When a will does not look like what your parent would have signed, South Carolina gives you a way to ask the court. It also gives you a deadline.",
   summary="Capacity, undue influence, fraud and execution challenges, and the deadlines to raise them.",
   body=(
       '<h2>Grounds to contest a will in South Carolina</h2>'
       + checks(["<b>Lack of testamentary capacity.</b> The person did not understand what they owned, who their family was, or what the will did—common with late-life dementia.",
                 "<b>Undue influence.</b> Someone in a position of trust—a caregiver, a new spouse, one child—substituted their wishes for the testator's. Isolation, a sudden change in the plan, and involvement in getting the will drafted are the classic signs.",
                 "<b>Fraud or forgery.</b> The signature is not genuine, or the person was deceived about what they were signing.",
                 "<b>Improper execution.</b> Missing or interested witnesses, unsigned pages, or a document that does not meet " + cite("will_execution", "S.C. Code § 62-2-502") + ".",
                 "<b>Revocation or a later will.</b> A newer valid will, or a physical act of revocation, replaced the one offered."]) +
       '<h2>Who can contest</h2>'
       '<p>An “interested person”—someone who would inherit more if the will failed: heirs under intestacy law, beneficiaries under an earlier will, and sometimes creditors. Being unhappy with a will is not enough; being harmed by it is.</p>'
       '<h2>Deadlines</h2>'
       '<p>A will admitted informally can be challenged in a formal proceeding, but generally only within the later of eight months after informal probate or one year after death; a will admitted formally after notice must be challenged by appeal. Once those windows close, the will stands. If you have received a notice from a probate court, the clock is already running—call before it stops.</p>'
       '<h2>How a contest proceeds</h2>'
       + steps([("Petition.", " A formal petition is filed in the probate court stating the grounds; the personal representative and beneficiaries are served."),
                ("Discovery.", " Medical records, the drafting attorney's file, bank records, witness statements. This is where most contests are won or lost."),
                ("Mediation.", " Probate courts routinely order it, and most contests settle here—often by adjusting shares rather than throwing out the will."),
                ("Trial.", " Before the probate judge or, on request, removed to circuit court for a jury. The contestant carries the burden on capacity and undue influence.")]) +
       '<h2>Defending a will</h2>'
       '<p>We also represent personal representatives and beneficiaries defending a will that reflects exactly what the person wanted—often a parent who chose to leave more to the child who cared for them. A well-drafted, properly witnessed, self-proved will with a lawyer\'s file behind it is hard to overturn.</p>'
       + band("Think a will is wrong?", "Bring the will, the notice and what you know about how it was signed. We will give you a candid read on the case and the deadline.")
   ),
   faqs=[
       ("What does a will contest cost?", "Contested matters are billed hourly with a written estimate. Some cases warrant a contingency arrangement; ask."),
       ("Can a no-contest clause stop me?", "South Carolina enforces them only against contests brought without probable cause. A contest with a genuine basis does not trigger the penalty."),
   ],
   related=["executor-disputes", "probate-process", "trust-administration"])

sp("guardianship-and-conservatorship", card_new=True,
   title="Guardianship & Conservatorship Attorney in Summerville, SC | Adults & Minors",
   description="Guardianship (person) and conservatorship (finances) for an incapacitated adult or a minor in Dorchester, Berkeley and Charleston County probate courts—including contested cases. Former probate judge Tara Frost.",
   h1="Guardianship and Conservatorship in Summerville, SC", nav_label="Guardianship & conservatorship",
   lead="When a parent can no longer manage safely, or a child needs a legal decision-maker, a court can appoint one. Here is how it works, which court does what, and how to avoid it when you can.",
   summary="Court-appointed decision-makers for adults who cannot manage and for minors—contested or not.",
   body=(
       answer("Frost Law Group handles guardianship and conservatorship petitions in the Dorchester, Berkeley and Charleston County probate courts, including contested cases where family members disagree about who should serve or whether the person is incapacitated. Tara L. Frost served as a Dorchester County Associate Probate Judge, where these cases are heard.", "Which attorneys in Summerville, SC handle contested guardianship cases?")
       + answer(f"Yes. We handle guardianship of minors when parents have died, are absent or cannot care for a child, and conservatorships to manage money a minor inherits or receives from a settlement. In South Carolina the Family Court appoints a guardian of a child’s person and the probate court appoints a conservator for the child’s money; our {A('guardianship-of-minors', 'guardianship of minors')} page explains both.", "Which Summerville, SC attorneys help with guardianship of minors?")
       + '<h2>Guardianship vs. conservatorship</h2>'
       + table(["", "Guardian", "Conservator"], [
           ["Decides about", "The person: housing, medical care, daily life", "The money: accounts, bills, property, benefits"],
           ["Appointed when", "An adult cannot make or communicate responsible personal decisions, or a minor needs a decision-maker", "An adult cannot manage finances, or a minor receives funds"],
           ["Court", "Probate court for adults; Family Court for a minor’s person", "Probate court, for adults and minors"],
           ["Ongoing duties", "Annual report on the person’s condition", "Inventory, bond, and annual accountings"],
       ]) +
       '<h2>Adult guardianship and conservatorship</h2>'
       f'<p>Under South Carolina’s adult guardianship and protective proceedings statutes ({cite("guardianship", "S.C. Code Title 62, Article 5")}), a petition is filed in probate court with medical evidence of incapacity. The court appoints a guardian ad litem and examiners to evaluate the person, notifies family members, and holds a hearing. The alleged incapacitated person has the right to counsel and to object. If incapacity is proven, the court appoints the guardian or conservator with the powers the person actually needs, no more, and may order a limited guardianship.</p>'
       '<h2>When families disagree</h2>'
       '<p>Contested cases arise when siblings each want to serve, when a parent objects to any guardian, or when one relative believes another is exploiting the parent. The court decides based on the person’s best interest and statutory priorities, with evidence about each candidate’s suitability. We prepare these cases the way the court evaluates them: medical proof, financial records, and a concrete plan for the person’s care.</p>'
       '<h2>Guardianship and conservatorship of minors</h2>'
       f'<p>Children are handled differently from adults, and by two different courts. A guardian of a minor’s <em>person</em>, the adult who has custody and makes daily decisions when parents have died or cannot act, is appointed by the Family Court, and a parent’s will can nominate that person. A <em>conservator</em> to manage money a child inherits or receives from a settlement is appointed by the probate court, which has exclusive jurisdiction over conservatorships. South Carolina’s minor-settlement statute ({ext("https://www.scstatehouse.gov/code/t62c005.php", "S.C. Code § 62-5-433")}) sets the thresholds: a settlement over $25,000 must be approved by the circuit court and paid through a conservator; $25,000 or less may be approved by the probate court or the circuit court; $2,500 or less needs no court approval at all. Our {A("guardianship-of-minors", "guardianship of minors")} page explains both tracks, the paperwork and the alternatives, including trusts that keep an inheritance out of a court-supervised account.</p>'
       '<h2>Avoiding a guardianship</h2>'
       f'<p>Most adult guardianships happen because no one signed a {A("power-of-attorney", "durable power of attorney and health care power of attorney")} while they could. If a parent still has capacity, even limited, fluctuating capacity, those documents may still be signed, and they are faster, cheaper and private. We will tell you honestly which path is available.</p>'
       '<h2>Serving as guardian or conservator</h2>'
       '<p>The role comes with reports, accountings, and personal responsibility for the person’s welfare or money. We help guardians and conservators file what the court requires, obtain permission for major decisions, and close the case when it ends.</p>'
       + band("Worried about a parent or a child?", "Call. We will tell you whether a guardianship is needed, whether a power of attorney can still be signed, and what the court will require.")
   ),
   faqs=[
       ("How long does a guardianship take in South Carolina?", "Uncontested adult cases commonly take two to four months from filing to hearing, depending on the county’s docket and how quickly examiners report. Emergency appointments are available when the person is in immediate danger."),
       ("Which court appoints a guardian for a child in South Carolina?", "The Family Court appoints a guardian of a minor’s person (custody and daily decisions). The probate court appoints a conservator to manage a minor’s money and approves settlements of $25,000 or less; larger settlements go to the circuit court."),
       ("Can a guardian move a parent to a facility?", "Generally yes, but South Carolina restricts certain placements and treatment decisions without additional court approval. The order sets the limits."),
       ("Does a guardian get paid?", "Family guardians often serve without pay; the court can approve reasonable compensation from the protected person’s funds."),
   ],
   related=["guardianship-of-minors", "power-of-attorney", "special-needs-planning"])

sp("trust-administration", card_new=True,
   title="Trust Administration & Inherited Assets in Summerville, SC | Trustee Duties",
   description="Help for trustees and beneficiaries after a death: trustee duties under the South Carolina Trust Code, notices and accountings, managing and distributing inherited assets, and resolving trust disputes. Summerville attorneys.",
   h1="Trust Administration and Inherited Assets in Summerville, SC", nav_label="Trust administration",
   lead="A trust avoids probate, but it does not administer itself. What a successor trustee must do, and how beneficiaries make sure it is done.",
   summary="Trustee duties, notices and accountings, and managing an inheritance.",
   body=(
       answer("Frost Law Group advises successor trustees on administering a trust after a death—notices, inventories, taxes, distributions and accountings under the South Carolina Trust Code—and helps beneficiaries manage or protect what they inherit, including inherited retirement accounts and real estate.", "Who can assist with managing inherited assets in Summerville, SC?")
       + '<h2>The successor trustee\'s job</h2>'
       + steps([("Accept the role and get the paperwork.", " A certification of trust, the death certificate and a tax ID for the now-irrevocable trust let you deal with banks and brokerages."),
                ("Notify beneficiaries.", f" South Carolina's Trust Code ({cite('trust_code', 'S.C. Code § 62-7-813')}) requires the trustee to keep qualified beneficiaries reasonably informed—including notice of the trust's existence, the trustee's contact information and the right to a copy of the trust."),
                ("Inventory and value.", " Everything the trust owns, at date-of-death value, which also sets the new income-tax basis for most assets."),
                ("Pay and file.", " Final expenses, valid debts, and the decedent's and trust's tax returns."),
                ("Distribute per the document.", " Outright shares, continuing trusts for young or vulnerable beneficiaries, or a marital trust—exactly as written, with receipts."),
                ("Account.", " Beneficiaries are entitled to a report of the trust's assets, liabilities, receipts and disbursements at least annually and at termination.")]) +
       '<h2>Managing what you inherit</h2>'
       + checks(["<b>Inherited retirement accounts</b> follow strict federal timing rules; most non-spouse beneficiaries must empty the account within ten years. The election you make in the first year matters.",
                 "<b>Inherited real estate</b> usually receives a stepped-up basis; keep the appraisal. Decide early whether to keep, rent or sell, and who pays carrying costs meanwhile.",
                 "<b>A continuing trust for you</b> means a trustee decides distributions; you have rights to information and to ask the court if the trustee is unreasonable.",
                 "<b>Inheritance and your own plan.</b> A large inheritance is the moment to review your own will, beneficiary designations and asset-protection planning."]) +
       '<h2>When trusts go wrong</h2>'
       '<p>A trustee who will not communicate, mixes trust money with their own, favors one beneficiary, or simply does nothing can be compelled to act or removed by the probate court. We represent beneficiaries in those petitions and trustees who need to respond to them.</p>'
       + band("Just became a trustee—or a beneficiary?", "Bring the trust and the account statements. We will give you the checklist and the deadlines.")
   ),
   faqs=[
       ("Does a trust go through probate?", "No, if it was funded. Assets left outside the trust in the decedent's name may still require probate or a small estate affidavit."),
       ("Can a trustee be paid?", "Yes, reasonable compensation as the trust provides or the Trust Code allows, and reimbursement of expenses."),
   ],
   related=["revocable-trust", "executor-disputes", "high-net-worth-estate-planning"])

sp("probate-courts", card_new=True,
   title="Dorchester, Berkeley and Charleston County Probate Courts | Which Court Has Your Case",
   description="Which probate court handles your family’s estate, guardianship or trust matter: Dorchester County (St. George), Berkeley County (Moncks Corner) or Charleston County (Broad Street), with addresses, phones, hours and a detailed guide for each court.",
   h1="Probate Courts Serving Summerville: Dorchester, Berkeley and Charleston Counties", nav_label="Probate courts guide",
   lead="Which court handles your family’s estate, guardianship or trust matter depends on where the person lived. Here is how to tell, where each court is, and a detailed guide to each one.",
   summary="Which of the three probate courts has your case, with a detailed guide for each.",
   body=(
       answer("Estates are opened in the probate court of the county where the person was domiciled at death; conservatorships and adult guardianships are filed where the person lives. Most Summerville addresses are in Dorchester County and file in St. George, but Nexton, Cane Bay and Carnes Crossroads are in Berkeley County and file in Moncks Corner. North Charleston, Charleston, Mount Pleasant and the islands file in Charleston County. Each court has its own intake routine, which the three guides below explain.", "The short answer")
       + '<h2>Which court has your case</h2>'
       '<p>Domicile, not the place of death or the location of the property, decides the county. A Summerville resident who died at MUSC is a Dorchester County estate; a Goose Creek resident who owned a lot in Dorchester County is a Berkeley County estate, and the Dorchester property is handled in it. A Summerville address can fall in Dorchester <em>or</em> Berkeley County, so check the county on the property tax bill or voter registration before filing. Only real estate in another state requires a second, ancillary proceeding there.</p>'
       '[[cards:dorchester-county-probate-court,berkeley-county-probate-court,charleston-county-probate-court]]'
       '<h2>The three courts at a glance</h2>'
       + table(["", "Dorchester County", "Berkeley County", "Charleston County"], [
           ["Where", "5200 E. Jim Bilton Blvd., St. George", "300-B California Ave., Moncks Corner", "84 Broad St., 3rd floor (estates) and 100 Broad St., Suite 469 (guardianships), Charleston"],
           ["Phone", "(843) 563-0105 or (843) 832-0105", "(843) 719-4519", "(843) 958-5030 estates; (843) 958-5180 guardianships"],
           ["Hours", "Mon–Fri 8:30 AM–5 PM", "Mon–Fri 9 AM–5 PM; walk-ins to 3:30 PM; drop box 9 AM–4 PM", "Mon–Fri 8:30 AM–5 PM; electronic filing at any hour"],
           ["Filing without a lawyer", "Opening Probate Worksheet, then a required Opening Probate Seminar", "Clerks review filings at the counter; no seminar", "Online estate appointments, free workshops and EZ-Filing"],
           ["Guide", A("dorchester-county-probate-court", "Dorchester County guide"), A("berkeley-county-probate-court", "Berkeley County guide"), A("charleston-county-probate-court", "Charleston County guide")],
       ]) +
       '<h2>What every court will ask for</h2>'
       + checks(["The original will, if any, and any codicils; the will must be delivered to the court within thirty days of death whether or not an estate is opened",
                 "A certified death certificate",
                 "Names and addresses of heirs and devisees",
                 "A preliminary list of assets and approximate values, and known debts",
                 "Photo identification and the filing fee, which is set by statute on a sliding scale"]) +
       '<h2>Fees are the same statewide</h2>'
       f'<p>Every South Carolina probate court charges the estate fee in {cite("probate_fees", "S.C. Code § 8-21-770")}, based on the inventory value: $25 under $5,000; $45 to $20,000; $67.50 to $60,000; $95 to $100,000; $95 plus 0.15 percent of the value between $100,000 and $600,000; and 0.25 percent of the value above $600,000 on top of that. Certified copies are $5. What differs by county is procedure: who must attend a seminar, whether filings can be e-filed, and how quickly letters issue.</p>'
       '<h2>Practical notes</h2>'
       + checks([f"Most filings use the statewide forms published by the {link('sccourts_probate_forms', 'South Carolina Judicial Branch')}; each court has local practices about scheduling and notice.",
                 "Hearings in contested matters are before the probate judge; a party may demand a jury trial in limited cases.",
                 "Clerks cannot give legal advice; they can tell you which form applies and whether a filing is complete.",
                 "Public estate records for all three counties are searchable online at southcarolinaprobate.net."]) +
       '<p>Court details were checked against the counties’ websites in October 2026. Call the court, or us, before you drive.</p>'
       + band("Not sure which court?", "Tell us the address and what needs to be filed. We will point you to the right courthouse and tell you what to bring.")
   ),
   faqs=[
       ("Can I file in Dorchester County if my father lived in Goose Creek?", "No. The estate is opened where he was domiciled: Berkeley County for most Goose Creek addresses."),
       ("Do I need to appear in person?", "For an uncontested informal estate, usually not; filings can be handled by mail, by e-filing in Charleston County, or through counsel. Dorchester County requires families filing without a lawyer to attend its Opening Probate Seminar. Contested matters and guardianships involve hearings."),
       ("Which county is Nexton in?", "Berkeley County, as are Cane Bay and Carnes Crossroads, despite their Summerville addresses. Estates for those residents are opened in Moncks Corner."),
   ],
   related=["probate-process", "small-estate-affidavit", "guardianship-and-conservatorship"])


# ----------------------------------------------------------------------------- COUNTY COURT GUIDES
sp("dorchester-county-probate-court", card_new=True,
   title="Dorchester County Probate Court Guide | St. George, SC | Hours, Fees and Filing",
   description="How to open an estate at the Dorchester County Probate Court in St. George: address, phone and hours, the Opening Probate Worksheet and seminar for families without a lawyer, forms, filing fees, the eight-month creditor period and when to call an attorney.",
   h1="Dorchester County Probate Court: A Guide for Summerville Families", nav_label="Dorchester County Probate Court", eyebrow="Probate · Dorchester County",
   lead="The court that handles most Summerville estates sits in St. George, half an hour up Highway 78. Tara Frost served there as an Associate Probate Judge. Here is how it works, from the first phone call to the closing statement.",
   summary="Address, hours, the worksheet-and-seminar rule, forms, fees and timelines at the St. George courthouse.",
   body=(
       answer("The Dorchester County Probate Court is at 5200 E. Jim Bilton Boulevard, St. George, SC 29477, open Monday through Friday from 8:30 AM to 5:00 PM, at (843) 563-0105 or (843) 832-0105. It handles estates, adult guardianships and conservatorships, conservatorships for minors, minor settlements of $25,000 or less, involuntary commitments and marriage licenses. A family opening an estate without an attorney must complete the court’s Opening Probate Worksheet and attend its Opening Probate Seminar before filing; an attorney files directly. Estate files can be searched online at southcarolinaprobate.net.", "The short answer")
       + '[[courts:dorchester_probate]]'
       + '<h2>Who files here</h2>'
       '<p>An estate is opened in the county where the person was domiciled at death, not where they died or where the property sits. Summerville proper, Knightsville, Lincolnville, Ridgeville, Harleyville, Reevesville, St. George and the Dorchester County side of Ladson all file in St. George. The exceptions trip people up: Nexton, Cane Bay, Carnes Crossroads and much of the Highway 17-A corridor carry Summerville addresses but lie in Berkeley County and file in Moncks Corner. The county on the property tax bill or voter registration settles it.</p>'
       '<h2>Before you file: the worksheet and the seminar</h2>'
       f'<p>Dorchester County is unusual in requiring preparation before a family files on its own. If the decedent lived in the county and died within the last ten years, a person who wants to open the estate without an attorney must download and complete the court’s {ext("https://www.dorchestercountysc.gov/government/courts-judicial-services/probate-court/estate-division", "Opening Probate Worksheet")}, print it and return it with the documents it lists. Once an estate clerk approves the worksheet, the court assigns a date for an Opening Probate Seminar, where staff explain the process and help complete the opening documents. A family that does not want to attend the seminar must retain an attorney. If more than ten years have passed since the death, the court must hold a hearing to determine heirs, with a formal petition, personal service on every heir, publication and a $150 filing fee; the court itself recommends a lawyer for that.</p>'
       '<h2>Opening an estate, step by step</h2>'
       + steps([
           ("Deliver the will.", f" Whoever holds the original will must deliver it to the court within thirty days of death ({cite('will_delivery', 'S.C. Code § 62-2-901')}), whether or not an estate is opened. The court files it for record (Form 306ES) for a $10 fee."),
           ("Apply for appointment.", " Form 300ES, the Application (Informal) or Petition (Formal) for Probate of Will or Appointment, with a certified death certificate, the original will, and the names and addresses of every heir and devisee. The personal representative named in the will has priority; without a will, the surviving spouse, then other heirs, in the order the Code sets."),
           ("Pay the fee.", f" The court collects $25 when the estate is opened and the balance of the estate fee under {cite('probate_fees', 'S.C. Code § 8-21-770')} when the inventory is filed. Fees run from $25 for estates under $5,000 to $95 plus 0.15 percent of the value between $100,000 and $600,000, and 0.25 percent above that."),
           ("Bond and waivers.", " A personal representative not excused by the will must post a fiduciary bond (Form 341ES) set by the court; heirs can sign waivers that reduce or eliminate the bond within the limits the court allows."),
           ("Receive the certificate of appointment.", " Letters are issued once the application is approved. Banks, the DMV and brokerages act on a certified copy ($5 each)."),
           ("Give notice.", f" Within thirty days of appointment the personal representative sends Form 305ES, Information to Heirs and Devisees, to everyone with an interest, and publishes notice to creditors once a week for three weeks in a county newspaper. Creditors have eight months from first publication to file claims ({cite('creditor_period', 'S.C. Code § 62-3-801')})."),
           ("File the inventory.", " Form 350ES, the Inventory and Appraisement, listing every probate asset at its date-of-death value, is due within ninety days of appointment, along with the balance of the filing fee."),
           ("Pay, distribute and close.", " After the creditor period, valid claims and taxes are paid, real estate passes by deed of distribution (Form 400ES) recorded with the Register of Deeds, and the estate closes with a proposal for distribution or an accounting and receipts. A straightforward Dorchester County estate typically closes ten to fourteen months after it opens."),
       ]) +
       '<h2>Small estates</h2>'
       f'<p>If the probate estate is $45,000 or less in personal property, the family can skip the steps above and file Form 420ES, the {A("small-estate-affidavit", "small estate affidavit")}, thirty days after death. The judge countersigns it and the certified affidavit is presented to the bank or the DMV. The same worksheet-and-seminar routine applies to families filing without a lawyer.</p>'
       '<h2>Guardianships, conservatorships and minors</h2>'
       f'<p>The court’s Therapeutic Division handles adult {A("guardianship-and-conservatorship", "guardianships and conservatorships")}: petitions with medical evidence, examiner and guardian ad litem reports, hearings, and the annual reports and accountings that follow. Conservatorships for minors who inherit or receive settlement money are filed here too, and the court approves {A("guardianship-of-minors", "minor settlements of $25,000 or less")}; larger settlements go to the circuit court. Guardians of a child’s person are appointed by the Family Court, not the probate court.</p>'
       '<h2>Getting there and what to expect</h2>'
       '<p>From Summerville, take Highway 78 west through Ridgeville to St. George, about thirty-five minutes; the courthouse complex is on E. Jim Bilton Boulevard with free parking. Call before you drive: hearings are by appointment, and the clerks can tell you whether a filing is complete, though not what to put in it. Dress as you would for church or a job interview.</p>'
       '<h2>Do you need a lawyer?</h2>'
       '<p>Not for every estate. A will that leaves everything to one person, heirs who agree, a house that will be sold and accounts that are easy to value can often be handled by a careful family member who attends the seminar and follows the forms. Call us when there is no will and the family tree is complicated, when real estate will be kept or divided, when an heir is a minor or has a disability, when creditors exceed the assets, when the personal representative lives out of state, or when anyone is unhappy. Tara Frost handled these files from the bench; she knows what the court will ask for and what delays it.</p>'
       + callout("<b>Frost first:</b> the court cannot tell you whether to open an estate, use an affidavit or do nothing. A ten-minute call with us can, and it is free.")
       + band("Opening an estate in Dorchester County?", "Bring the will and a list of what was owned. We will tell you which route fits, what it will cost, and how long it will take.")
   ),
   faqs=[
       ("Where is the Dorchester County Probate Court?", "5200 E. Jim Bilton Boulevard, St. George, SC 29477, in the county courthouse complex, open Monday through Friday from 8:30 AM to 5:00 PM. Phone (843) 563-0105 or (843) 832-0105."),
       ("Is there a probate office in Summerville?", "No. Although most Dorchester County residents live in the Summerville area, probate filings and hearings are in St. George. The Summerville magistrate’s office on Deming Way does not handle estates."),
       ("How much does it cost to probate an estate in Dorchester County?", "The statutory filing fee ranges from $25 for estates under $5,000 to $95 plus 0.15 percent of the value between $100,000 and $600,000, with 0.25 percent above that. The court collects $25 when the estate opens and the balance at the inventory, plus the newspaper’s charge for the creditor notice and $5 per certified copy."),
       ("How long does probate take in Dorchester County?", "No estate closes in less than eight months because of the creditor period. Routine estates typically close in ten to fourteen months; estates with real estate to sell, disputes or tax returns take longer."),
       ("Can I look up a Dorchester County estate online?", "Yes. Public estate records are searchable at southcarolinaprobate.net by selecting Dorchester Probate and entering the case number or the decedent’s last name."),
   ],
   related=["probate-process", "small-estate-affidavit", "berkeley-county-probate-court"])

sp("berkeley-county-probate-court", card_new=True,
   title="Berkeley County Probate Court Guide | Moncks Corner, SC | Hours, Fees and Filing",
   description="How to open an estate at the Berkeley County Probate Court in Moncks Corner: address, phone and hours, walk-in and drop-box rules, forms, filing fees, the eight-month creditor period, and when a Goose Creek, Nexton or Cane Bay family needs a lawyer.",
   h1="Berkeley County Probate Court: A Guide for Goose Creek, Nexton and Cane Bay Families", nav_label="Berkeley County Probate Court", eyebrow="Probate · Berkeley County",
   lead="Goose Creek, Hanahan, Moncks Corner, Daniel Island and the Berkeley County side of Summerville all file in Moncks Corner. Here is where the court is, how it takes filings, and what an estate costs and takes.",
   summary="Address, hours, walk-in and drop-box rules, forms, fees and timelines at the Moncks Corner courthouse.",
   body=(
       answer("The Berkeley County Probate Court is at 300-B California Avenue, Moncks Corner, SC 29461, (843) 719-4519, open Monday through Friday from 9:00 AM to 5:00 PM; walk-in filings are taken until 3:30 PM, and a drop box at the front of the courthouse accepts documents from 9:00 AM to 4:00 PM. The court has Estate, Guardian/Conservator, Therapeutic and Marriage License divisions. Guardians for children are appointed by the Family Court, not the probate court. Clerks help with forms at the counter but cannot give legal advice.", "The short answer")
       + '[[courts:berkeley_probate]]'
       + '<h2>Who files here</h2>'
       '<p>An estate is opened in the county where the person was domiciled at death. Goose Creek, Hanahan, Moncks Corner, Daniel Island, Huger, Bonneau, St. Stephen and the Berkeley County side of Ladson file here, and so do the Summerville-address communities that sit across the county line: Nexton, Cane Bay, Carnes Crossroads, Sangaree and much of the Highway 17-A and Highway 176 corridors. Thousands of families moved into those neighborhoods in the last decade, and many assume Dorchester County. The county on the property tax bill or voter registration settles it, and filing in the wrong county costs weeks.</p>'
       '<h2>How the court takes filings</h2>'
       f'<p>Berkeley County does not require a worksheet or seminar before a family files. Bring the documents to the counter during walk-in hours and an estate clerk will review them for completeness, or leave them in the drop box between 9:00 AM and 4:00 PM and the court will contact you. Hearings in contested matters are set by the court. The judge’s letter on the {link("berkeley_probate_site", "court’s website")} says it plainly: the clerks are capable and courteous, they cannot give legal advice, and the court recommends an attorney when you need legal assistance.</p>'
       '<h2>Opening an estate, step by step</h2>'
       + steps([
           ("Deliver the will.", f" The original will must be delivered to the court within thirty days of death ({cite('will_delivery', 'S.C. Code § 62-2-901')}), whether or not an estate is opened."),
           ("Apply for appointment.", " Form 300ES, the Application (Informal) or Petition (Formal) for Probate of Will or Appointment, with a certified death certificate, the original will and the names and addresses of every heir and devisee. The person named in the will has priority; without a will, the surviving spouse, then the other heirs."),
           ("Pay the fee.", f" The estate fee under {cite('probate_fees', 'S.C. Code § 8-21-770')} is based on the inventory value, from $25 for estates under $5,000 to $95 plus 0.15 percent of the value between $100,000 and $600,000 and 0.25 percent above that. The court collects an initial $25 and the balance when the inventory is filed."),
           ("Bond and waivers.", " A personal representative not excused by the will posts a fiduciary bond (Form 341ES); heirs may sign waivers."),
           ("Receive the certificate of appointment.", " Letters issue once the application is approved; certified copies are $5 each."),
           ("Give notice.", f" Within thirty days, Form 305ES to heirs and devisees, and a notice to creditors published once a week for three weeks in a Berkeley County newspaper. Creditors have eight months from first publication ({cite('creditor_period', 'S.C. Code § 62-3-801')})."),
           ("File the inventory.", " Form 350ES within ninety days of appointment, with the balance of the fee."),
           ("Pay, distribute and close.", " Claims and taxes are paid after the creditor period, real estate passes by deed of distribution (Form 400ES) recorded with the Berkeley County Register of Deeds, and the estate closes on an accounting or a proposal for distribution with receipts. Routine estates close in roughly ten to fourteen months."),
       ]) +
       '<h2>Small estates</h2>'
       f'<p>If the probate estate is $45,000 or less in personal property, Form 420ES, the {A("small-estate-affidavit", "small estate affidavit")}, can be filed thirty days after death and countersigned by the judge instead of opening an estate. The fee follows the same schedule, from $25 to $67.50.</p>'
       '<h2>Guardianships, conservatorships and minors</h2>'
       f'<p>The Guardian/Conservator Division oversees adult {A("guardianship-and-conservatorship", "guardianships and conservatorships")} and conservatorships for minors who inherit or receive settlement money, and the court approves {A("guardianship-of-minors", "minor settlements of $25,000 or less")}. Guardians of a child’s person are appointed by the Berkeley County Family Court, which sits in the same courthouse complex.</p>'
       '<h2>Getting there</h2>'
       '<p>From Summerville, take Highway 17-A north through Carnes Crossroads to Moncks Corner, about thirty minutes; from Goose Creek, Highway 52 north, about twenty. The courthouse is on California Avenue off Highway 52 with free parking, and the drop box is at the front entrance. Hearings are by appointment; call before you drive.</p>'
       '<h2>Do you need a lawyer?</h2>'
       '<p>Not for every estate. Berkeley County’s clerks are helpful, and a simple estate with a clear will and cooperative heirs can be handled by a careful family member. Call us when there is no will and the heirs are not obvious, when real estate will be kept or divided among several people, when an heir is a minor or has a disability, when debts may exceed assets, when the personal representative lives out of state, or when a family member is already unhappy. Tara Frost sat as a probate judge in the neighboring county; the Code and the forms are the same.</p>'
       + callout("<b>Frost first:</b> if you are not sure whether the home is in Berkeley or Dorchester County, send us the address. We will tell you which court, and whether an estate is needed at all.")
       + band("Opening an estate in Berkeley County?", "Bring the will and a list of what was owned. We will tell you which route fits, what it will cost, and how long it will take.")
   ),
   faqs=[
       ("Where is the Berkeley County Probate Court?", "300-B California Avenue, Moncks Corner, SC 29461, in the county courthouse. Phone (843) 719-4519. Open Monday through Friday from 9:00 AM to 5:00 PM, with walk-in filings until 3:30 PM."),
       ("My address says Summerville. Do I file in Berkeley County?", "If the home is in Nexton, Cane Bay, Carnes Crossroads, Sangaree or another Berkeley County neighborhood with a Summerville mailing address, yes. The county on the property tax bill controls, not the post office."),
       ("How much does probate cost in Berkeley County?", "The same statutory fee as every South Carolina county: $25 for estates under $5,000 up to $95 plus 0.15 percent of the value between $100,000 and $600,000, and 0.25 percent above that, plus the newspaper’s charge for the creditor notice and $5 per certified copy."),
       ("Who appoints a guardian for a child in Berkeley County?", "The Family Court. The probate court appoints conservators to manage a child’s money and approves minor settlements of $25,000 or less."),
       ("Can I file by drop box or mail?", "The drop box at the front of the courthouse accepts documents from 9:00 AM to 4:00 PM. Call the court before mailing an original will; deliver it in person or by a method that tracks delivery."),
   ],
   related=["probate-process", "dorchester-county-probate-court", "charleston-county-probate-court"])

sp("charleston-county-probate-court", card_new=True,
   title="Charleston County Probate Court Guide | 84 Broad Street | EZ-Filing, Fees and Forms",
   description="How to open an estate at the Charleston County Probate Court: the Estate Division at 84 Broad Street, the guardianship division at 100 Broad Street, EZ-Filing, estate appointments and free workshops, filing fees, forms and the eight-month creditor period.",
   h1="Charleston County Probate Court: A Guide for Families", nav_label="Charleston County Probate Court", eyebrow="Probate · Charleston County",
   lead="The busiest probate court in the Lowcountry opens about 2,200 estates a year from two buildings on Broad Street. Here is which one you need, how its electronic filing works, and what an estate costs and takes.",
   summary="Two Broad Street locations, EZ-Filing, appointments and workshops, forms, fees and timelines.",
   body=(
       answer("The Charleston County Probate Court’s Estate Division is on the third floor of the Historic Courthouse at 84 Broad Street, Charleston, SC 29401, (843) 958-5030. Its Commitment and Guardianship Division is in the Judicial Center at 100 Broad Street, Suite 469, (843) 958-5180. Both are open Monday through Friday from 8:30 AM to 5:00 PM, and the court accepts filings electronically at any hour through EZ-Filing. Families can book estate appointments online and attend the court’s free estate administration and planning workshops. Charleston, North Charleston, Mount Pleasant, West Ashley, James Island, Johns Island and the beach towns file here; Daniel Island is in Berkeley County.", "The short answer")
       + '[[courts:charleston_probate]]'
       + '<h2>Which building you need</h2>'
       + table(["Matter", "Where", "Phone"], [
           ["Estates, wills, small estate affidavits, trust disputes", "Estate Division, Historic Courthouse, 84 Broad Street, 3rd floor", "(843) 958-5030"],
           ["Adult guardianships and conservatorships, conservatorships for minors, commitments", "Commitment and Guardianship Division, Judicial Center, 100 Broad Street, Suite 469", "(843) 958-5180"],
           ["Marriage licenses", "Judicial Center, 100 Broad Street, Suite 469", "(843) 958-5183"],
       ]) +
       '<p>Drop boxes outside both offices accept documents after hours. Public estate and will records are searchable online at southcarolinaprobate.net.</p>'
       '<h2>Who files here</h2>'
       '<p>An estate is opened in the county where the person was domiciled at death. Charleston, North Charleston, Mount Pleasant, West Ashley, James Island, Johns Island, Wadmalaw Island, Folly Beach, Sullivan’s Island, Isle of Palms, Ravenel, Hollywood, Meggett, McClellanville and Awendaw all file here. Daniel Island is part of the City of Charleston but lies in Berkeley County, so a Daniel Island resident’s estate is opened in Moncks Corner. Hanahan and Goose Creek are Berkeley County as well.</p>'
       '<h2>EZ-Filing, appointments and workshops</h2>'
       f'<p>Charleston County runs the most automated probate court in the region. Under an administrative order, documents are filed electronically through {ext("https://ez-filing.net/southcarolina/", "EZ-Filing")}; an account also lets you view every image on your case, which is the easiest way to keep up with what has been filed. Original wills must still be delivered to the court. Families handling an estate themselves can book an estate appointment with staff through the link on the {link("charleston_probate_site", "court’s website")} and sign up for its free virtual and in-person workshops on estate administration and estate planning. The court also runs a mental health court, drug courts and a veterans treatment court, which is why the Judicial Center lobby is busier than you expect.</p>'
       '<h2>Opening an estate, step by step</h2>'
       + steps([
           ("Deliver the will.", f" The original will must be delivered to the Estate Division within thirty days of death ({cite('will_delivery', 'S.C. Code § 62-2-901')}), whether or not an estate is opened."),
           ("Apply for appointment.", " Form 300ES, the Application (Informal) or Petition (Formal) for Probate of Will or Appointment, with a certified death certificate, the original will and the names and addresses of every heir and devisee, filed through EZ-Filing or at the counter."),
           ("Pay the fee.", f" The estate fee under {cite('probate_fees', 'S.C. Code § 8-21-770')} is based on the inventory value, from $25 for estates under $5,000 to $95 plus 0.15 percent of the value between $100,000 and $600,000 and 0.25 percent above that. Charleston County estates are often in the upper tiers because of real estate values: a $700,000 estate pays $1,095."),
           ("Bond and waivers.", " A personal representative not excused by the will posts a fiduciary bond (Form 341ES); heirs may waive it."),
           ("Receive the certificate of appointment.", " Letters issue once the application is approved; certified copies are $5 each."),
           ("Give notice.", f" Within thirty days, Form 305ES to heirs and devisees, and a notice to creditors published once a week for three weeks in a Charleston County newspaper; the newspaper’s charge is typically $40 to $120. Creditors have eight months from first publication ({cite('creditor_period', 'S.C. Code § 62-3-801')})."),
           ("File the inventory.", " Form 350ES within ninety days of appointment, with the balance of the fee."),
           ("Pay, distribute and close.", " Claims and taxes are paid after the creditor period, real estate passes by deed of distribution (Form 400ES) recorded with the Charleston County Register of Deeds at 101 Meeting Street, and the estate closes on an accounting or a proposal for distribution with receipts. Routine estates close in roughly ten to fourteen months; estates with downtown or island real estate to sell take longer."),
       ]) +
       '<h2>Small estates</h2>'
       f'<p>If the probate estate is $45,000 or less in personal property, Form 420ES, the {A("small-estate-affidavit", "small estate affidavit")}, can be filed thirty days after death and countersigned by the judge instead of opening an estate. Given Charleston County property values, the affidavit usually works only when the real estate was jointly owned or in a trust.</p>'
       '<h2>Guardianships, conservatorships and minors</h2>'
       f'<p>The Commitment and Guardianship Division at 100 Broad Street handles adult {A("guardianship-and-conservatorship", "guardianships and conservatorships")}, conservatorships for minors, and the court’s approval of {A("guardianship-of-minors", "minor and wrongful death settlements")}; settlements for a minor over $25,000 go to the circuit court in the same building. Guardians of a child’s person are appointed by the Charleston County Family Court.</p>'
       '<h2>Getting there</h2>'
       '<p>Both buildings are at the Four Corners of Law, Broad and Meeting Streets, downtown. From Summerville allow forty-five minutes on I-26 to the Meeting Street exit; from Mount Pleasant, the Ravenel Bridge to East Bay and Broad. Street parking is metered and scarce; the city garages on Cumberland and Queen Streets are the practical choice. Security screening is required at both entrances, so leave time.</p>'
       '<h2>Do you need a lawyer?</h2>'
       f'<p>Not for every estate. Charleston County’s appointments and workshops make a simple estate manageable for a careful family member. Call us when there is downtown, island or rental real estate to keep, sell or divide; when heirs are out of state or out of the country; when there is no will and the family is complicated; when an heir is a minor or has a disability; when a business or heirs’ property is involved; or when anyone is already unhappy. Our {A("probate-attorney-charleston-sc", "Charleston probate page")} explains how we handle estates in this court from Summerville, thirty minutes away.</p>'
       + callout("<b>Frost first:</b> before you create an EZ-Filing account and start filing, call. Ten minutes on the phone tells you whether the estate needs full probate, an affidavit or nothing at all.")
       + band("Opening an estate in Charleston County?", "Bring the will and a list of what was owned. We will tell you which route fits, what it will cost, and how long it will take.")
   ),
   faqs=[
       ("Where is the Charleston County Probate Court?", "The Estate Division is on the third floor of the Historic Courthouse at 84 Broad Street, (843) 958-5030. Guardianships, conservatorships, commitments and marriage licenses are in the Judicial Center at 100 Broad Street, Suite 469, (843) 958-5180. Both are open Monday through Friday from 8:30 AM to 5:00 PM."),
       ("Can I file probate documents online in Charleston County?", "Yes. The court’s EZ-Filing system accepts filings electronically, and an account lets you view the documents on your case. Original wills must still be delivered to the court."),
       ("How much does probate cost in Charleston County?", "The statutory fee ranges from $25 for estates under $5,000 to $95 plus 0.15 percent of the value between $100,000 and $600,000, and 0.25 percent above that: $845 for a $600,000 estate and $1,095 for a $700,000 estate, plus the creditor notice and $5 per certified copy."),
       ("Does the court help families without a lawyer?", "Yes. Estate appointments can be booked online, and the court runs free virtual and in-person estate administration and planning workshops. Staff cannot give legal advice."),
       ("Is Daniel Island in Charleston County?", "No. Daniel Island is part of the City of Charleston but lies in Berkeley County, so a Daniel Island resident’s estate is opened at the Berkeley County Probate Court in Moncks Corner."),
   ],
   related=["probate-attorney-charleston-sc", "probate-process", "dorchester-county-probate-court"])

# ----------------------------------------------------------------------------- MINORS AND CHARLESTON
sp("guardianship-of-minors", card_new=True,
   title="Guardianship of a Minor in South Carolina | Family Court, Conservators and Settlements",
   description="How guardianship of a minor works in South Carolina: the Family Court appoints a guardian of the child’s person, the probate court appoints a conservator for the child’s money, and settlements are approved under the $2,500 and $25,000 thresholds in § 62-5-433. Summerville attorneys.",
   h1="Guardianship of a Minor in South Carolina: Who Decides, Who Holds the Money", nav_label="Guardianship of minors",
   lead="When a child’s parents have died or cannot care for them, or when a child receives money, two different courts may be involved. Here is which court does what, what the dollar thresholds are, and how a parent’s will can shape the outcome.",
   summary="Family Court guardianship, probate conservatorship, the $2,500 and $25,000 settlement thresholds, and the alternatives.",
   body=(
       answer(f"In South Carolina a guardian of a minor’s <em>person</em>, the adult with custody who makes daily decisions, is appointed by the Family Court, and a parent’s will can nominate who that should be. A <em>conservator</em> to hold and manage a child’s money is appointed by the probate court, which has exclusive jurisdiction over conservatorships ({cite('guardianship', 'S.C. Code Title 62, Article 5')}). When a child receives a settlement, {ext('https://www.scstatehouse.gov/code/t62c005.php', 'S.C. Code § 62-5-433')} sets the rules: $2,500 or less can be handled by a parent without court approval; $25,000 or less can be approved by the probate court or the circuit court; more than $25,000 must be approved by the circuit court and paid through a conservator or a protective order. Money held by a conservator is released when the child turns eighteen.", "The short answer")
       + '<h2>Two courts, two questions</h2>'
       + table(["", "Guardian of the person", "Conservator (the money)"], [
           ["Decides", "Where the child lives, school, medical care, daily life", "Inheritances, insurance proceeds, settlement money, property"],
           ["Appointed by", "The Family Court of the county where the child lives", "The probate court of the county where the child lives"],
           ["Nominated by", "A parent’s will or written designation; the court still decides best interest", "A parent’s will may name one; the court appoints"],
           ["Ends", "At eighteen, marriage, adoption, or when a parent resumes custody", "At eighteen, when the funds are delivered to the former minor"],
       ]) +
       '<h2>Guardianship of the person: the Family Court</h2>'
       '<p>When both parents have died, when a parent is deployed, incarcerated, in treatment or otherwise unable to care for a child, or when a child has been living with a grandparent and a school or physician wants legal authority, the Family Court can appoint a guardian or award custody to the relative. A parent can nominate a guardian in a will, and courts give that nomination great weight, but the decision is always the child’s best interest. The person named has to accept and be approved, which is why a well-drafted will names an alternate. In Dorchester, Berkeley and Charleston counties these petitions are filed with the Family Court clerk in St. George, Moncks Corner and Charleston.</p>'
       '<h2>Conservatorship: the probate court</h2>'
       '<p>A child cannot legally receive more than modest sums directly. When a minor inherits outright, is the beneficiary of a life insurance policy, or receives settlement money, the probate court appoints a conservator, usually a parent, to hold it. The conservator posts a bond or places the funds in a restricted account, files an inventory, asks the court’s permission before spending principal, files an annual accounting, and turns the money over when the child turns eighteen. It is protective, and it is also rigid: the court decides whether the money can pay for braces or a car, and an eighteen-year-old receives the balance whether or not they are ready for it.</p>'
       '<h2>Settlements for children: the thresholds</h2>'
       + table(["Net amount to the child", "Who approves", "Where the money goes"], [
           ["$2,500 or less", "No court approval; the parent or guardian signs the release", "To the parent or guardian for the child"],
           ["More than $2,500, up to $25,000", "The probate court or the circuit court, on a verified petition by the guardian or guardian ad litem (an existing conservator may settle without approval)", "As § 62-5-103 allows: modest amounts to the parent or custodian, larger sums to a conservator or a court-approved arrangement"],
           ["More than $25,000", "The circuit court only, on a verified petition stating that the settlement is in the child’s best interest", "Through a conservator appointed by the probate court, or under a probate court protective order"],
       ]) +
       '<p>In practice: a car-crash settlement of $40,000 for a child in Summerville means a petition in the Dorchester County circuit court, a conservatorship opened in the Dorchester County Probate Court, a bond or a restricted account, an inventory and an annual accounting until the child turns eighteen. A $15,000 settlement can be approved in the probate court, often with the funds placed in a restricted account the child receives at eighteen. Structured settlements that pay out over time, and settlements placed in a trust the court approves, can soften both the rigidity and the eighteenth-birthday problem.</p>'
       '<h2>Avoiding a conservatorship with a plan</h2>'
       + checks([f"<b>Name a guardian and a trustee in your {A('last-will-and-testament', 'will')}.</b> A testamentary trust holds the children’s inheritance under a trustee you choose, with distributions at the ages you choose, instead of a court-supervised account released at eighteen.",
                 "<b>Make life insurance and retirement accounts payable to the trust</b>, not to a minor child directly. A child named as beneficiary means a conservatorship.",
                 "<b>Custodial (UTMA) accounts</b> for modest gifts; South Carolina releases them at eighteen or twenty-one depending on how the account was created.",
                 f"<b>A {A('special-needs-planning', 'special needs trust')}</b> for a child with a disability, so an inheritance or settlement does not cost the child SSI or Medicaid.",
                 "<b>Choose the guardian and the money manager separately.</b> The best person to raise your children is not always the best person to manage money, and the two roles can check each other."]) +
       '<h2>Grandparents and relatives raising a child</h2>'
       '<p>Many Lowcountry grandparents raise grandchildren with no paperwork at all until a school, a doctor or an insurer asks for authority. Options range from a limited written delegation of parental powers signed by the parent, to a Family Court custody or guardianship order, to adoption. Which one fits depends on whether the parent agrees, how long the arrangement will last and whether benefits are involved. We will tell you the least drastic option that actually works.</p>'
       + callout("<b>Frost first:</b> if a child in your family is about to receive money from an estate, an insurance policy or a settlement, call before anything is paid. The order of operations decides whether the child gets a conservatorship, a trust or nothing more than a bank account.")
       + band("A child in your family needs a decision-maker, or is receiving money?", "Call. We will tell you which court is involved, what the thresholds mean for your situation, and whether a trust can keep it simple.")
   ),
   faqs=[
       ("Which court handles guardianship of a minor in South Carolina?", "The Family Court appoints a guardian of a child’s person. The probate court appoints a conservator for a child’s money and approves settlements of $25,000 or less; settlements over $25,000 are approved by the circuit court."),
       ("Can a parent name a guardian in a will?", "Yes. A will can nominate a guardian for minor children, and the court gives the nomination great weight, but it still decides based on the child’s best interest. Name an alternate, and consider a trust so the guardian is not also managing a court-supervised account."),
       ("At what amount does a child’s settlement need court approval?", "Anything over $2,500. Up to $25,000 the probate court or the circuit court can approve it; over $25,000 only the circuit court can, and the money must go through a conservator or a protective order."),
       ("When does a child get the money?", "A conservator delivers the funds when the child turns eighteen. A trust in a parent’s will can set a later age or stage the distributions, which is the main reason to plan rather than let the court hold the money."),
       ("Does a grandparent raising a grandchild need a guardianship?", "Often not for day-to-day life, but schools, doctors and insurers increasingly require legal authority. A Family Court guardianship or custody order, or a limited written delegation from the parent, solves that."),
   ],
   related=["guardianship-and-conservatorship", "last-will-and-testament", "special-needs-planning"])

sp("probate-attorney-charleston-sc", card_new=True,
   title="Probate Attorney Serving Charleston, SC | Estates in the Charleston County Probate Court",
   description="Probate and estate administration in the Charleston County Probate Court for Charleston, North Charleston, Mount Pleasant, West Ashley and the islands, from a former Dorchester County probate judge thirty minutes up I-26. Opening the estate, creditors, real estate, disputes.",
   h1="Probate Attorney Serving Charleston, SC", nav_label="Charleston probate", eyebrow="Probate · Charleston County",
   lead="Charleston County estates are opened on Broad Street and administered under statewide rules that a former probate judge knows from the bench. We handle them for families across the county, and we are honest about which ones you can handle yourself.",
   summary="Estate administration, disputes and guardianship in the Charleston County Probate Court.",
   body=(
       answer("Frost Law Group handles probate and estate administration in the Charleston County Probate Court: opening the estate, guiding the personal representative through notices, the inventory and the creditor period, selling or distributing real estate, resolving disputes among heirs, and closing. Tara Frost served as a Dorchester County Associate Probate Judge, and the Probate Code she applied from the bench is the same code the Charleston court applies. Our office is in Summerville, about thirty minutes from Broad Street, and most of a Charleston estate can be handled by phone, e-mail and the court’s EZ-Filing system.", "The short answer")
       + '<h2>What we do in a Charleston County estate</h2>'
       + checks([f"<b>Open the estate correctly.</b> Application, will, bond or waivers, and the certificate of appointment, filed through EZ-Filing so letters issue without a second trip. See the {A('probate-process', 'South Carolina probate process')}.",
                 f"<b>Guide the personal representative.</b> The {A('executor-duties', 'duties, deadlines and liabilities')} of a personal representative are the same statewide: notice to heirs within thirty days, the inventory within ninety, the eight-month creditor period, taxes, and an accounting.",
                 "<b>Handle the real estate.</b> Deeds of distribution recorded at the Charleston County Register of Deeds, sales during administration, rental property that keeps producing income while the estate is open, and the deed and title problems that surface when a family has owned land on Johns Island or Wadmalaw for generations.",
                 f"<b>Resolve disputes.</b> {A('executor-disputes', 'Accountings, removal petitions and self-dealing claims')}, {A('will-contests', 'will contests')} and trust disputes, tried before the probate judge or, on demand, a jury. The Charleston court tries hundreds of litigated cases a year.",
                 f"<b>Small estates and summary administration</b> when the probate estate is under $45,000 or the real estate is already in a trust, using the {A('small-estate-affidavit', 'small estate affidavit')}.",
                 f"<b>Guardianships and conservatorships</b> in the court’s Commitment and Guardianship Division at 100 Broad Street, including {A('guardianship-of-minors', 'conservatorships for minors and settlement approvals')}."]) +
       '<h2>The court, briefly</h2>'
       f'<p>Estates are opened in the Estate Division on the third floor of the Historic Courthouse at 84 Broad Street; guardianships and conservatorships are in the Judicial Center across the street at 100 Broad Street, Suite 469. Both are open weekdays from 8:30 AM to 5:00 PM, and filings go in electronically through EZ-Filing. Our {A("charleston-county-probate-court", "guide to the Charleston County Probate Court")} covers addresses, phones, fees, forms and the court’s free workshops.</p>'
       '[[courts:charleston_probate]]'
       '<h2>Charleston estates have Charleston problems</h2>'
       + checks(["<b>Real estate values push fees and taxes up.</b> The estate fee is $845 for a $600,000 estate and $1,095 at $700,000, and a downtown or island home often needs an appraisal, a decision about selling during administration, and flood insurance kept in force meanwhile.",
                 "<b>Heirs’ property.</b> Land passed down for generations without probate, with dozens of cousins holding fractional shares, is common on Johns Island, Wadmalaw and in the Sea Island communities. Clearing it means opening the estates that were never opened, sometimes several at once.",
                 "<b>Heirs out of state or overseas.</b> Charleston families are scattered. Waivers, renunciations and receipts have to be signed and notarized wherever the heirs are, and a personal representative who lives out of state may need a resident agent.",
                 "<b>Second homes and rentals.</b> Short-term rental income, property managers, HOA dues and the question of who pays carrying costs until distribution all need decisions in the first month.",
                 "<b>Ancillary estates.</b> When someone who lived in another state dies owning Charleston County real estate, a second, ancillary proceeding is opened here to pass title. We handle those for out-of-state families and their lawyers."]) +
       '<h2>What it costs</h2>'
       '<p>Court fees are set by statute and paid from the estate. Our fee is usually a flat fee for an uncontested estate, quoted after we see the will and the asset list, and it is paid from the estate as an administration expense, not from the family’s pocket. Contested matters are billed by the hour with an estimate up front.</p>'
       '<h2>Do you need a lawyer?</h2>'
       '<p>Not always, and we say so. A will that leaves everything to one person, a house that will be sold, cooperative heirs and simple accounts can be handled by a careful family member who uses the court’s estate appointments and workshops. Call us when real estate will be kept or divided, when heirs are far away or at odds, when there is no will and the family is complicated, when a business or heirs’ property is involved, or when a creditor, a caregiver or a sibling has already raised an objection.</p>'
       + band("Settling an estate in Charleston County?", "Bring the will and a list of what was owned. We will tell you whether you need us, what it would cost, and what to do this week.")
   ),
   faqs=[
       ("Do you handle probate in Charleston County from Summerville?", "Yes. Charleston County estates are filed electronically through EZ-Filing, and most of the work is documents, notices and phone calls. We go to Broad Street for hearings and when a family prefers to meet there."),
       ("How long does probate take in Charleston County?", "At least eight months because of the creditor period; routine estates close in ten to fourteen months, and estates with real estate to sell or disputes take longer."),
       ("What does a probate lawyer cost in Charleston, SC?", "Uncontested estates are usually a flat fee quoted after we see the will and the assets, paid from the estate. Contested matters are hourly with an estimate. Court fees are separate and set by statute."),
       ("What is heirs’ property?", "Land that passed through generations without wills or probate, so title sits in the names of long-dead owners and their many descendants. Clearing it requires opening the estates that were skipped, and sometimes a partition action. It is common in Charleston County’s Sea Island communities."),
   ],
   related=["charleston-county-probate-court", "probate-process", "executor-duties"])
