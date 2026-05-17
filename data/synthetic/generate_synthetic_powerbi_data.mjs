import { mkdir, writeFile } from "node:fs/promises";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const root = dirname(fileURLToPath(import.meta.url));

const projects = [
  ["P001", "Ukraine Health+ Response", "Ukraine", "Kyiv", "Kyiv Base", "Health", "In-kind"],
  ["P002", "Ukraine Winter CVA", "Ukraine", "Lviv", "Lviv Branch", "CVA", "Cash"],
  ["P003", "Poland Refugee CVA", "Poland", "Warsaw", "Warsaw Branch", "CVA", "Cash"],
  ["P004", "Sudan Food Security & WASH", "Sudan", "Port Sudan", "Port Sudan Base", "WASH", "Service delivery"],
  ["P005", "Venezuela-Colombia Multi-Donor Response", "Venezuela/Colombia", "Bogota", "Bogota Office", "Multi-sector", "Service delivery"],
  ["P006", "Syria Health Mission Support", "Syria", "Damascus", "Damascus Mission Office", "Health", "Support"]
];

const donors = [
  ["D001", "ECHO", "EUR"], ["D002", "BMZ", "EUR"], ["D003", "GFFO", "EUR"],
  ["D004", "UNICEF", "USD"], ["D005", "USAID", "USD"], ["D006", "AECID", "EUR"],
  ["D007", "EU Delegation", "EUR"], ["D008", "Red Cross Movement", "CHF"],
  ["D009", "Private Foundation", "USD"], ["D010", "Own Funds", "EUR"]
];

const budgetLines = [
  ["BL001", "Human Resources", "National staff salaries"],
  ["BL003", "Programme Supplies", "Medical and programme supplies"],
  ["BL004", "CVA Transfers", "Unconditional cash transfers"],
  ["BL005", "CVA Transfers", "Winter cash top-up"],
  ["BL006", "WASH Infrastructure", "Water point rehabilitation"],
  ["BL007", "Health Services", "Primary health service support"],
  ["BL008", "Logistics & Transport", "Vehicle rental and fuel"],
  ["BL009", "Training & Capacity Building", "Branch and partner training"],
  ["BL010", "Monitoring & Evaluation", "PDM and field monitoring"],
  ["BL011", "Administration", "Office running costs"],
  ["BL012", "Audit & Compliance", "External audit and compliance checks"],
  ["BL014", "Indirect Costs", "Indirect cost recovery"]
];

const docs = ["Complete", "Complete", "Complete", "Partial", "Missing"];
const procurement = ["Complete", "Complete", "In progress", "Gap identified"];
const reporting = ["On time", "On time", "On time", "Late"];
const risks = ["Low", "Low", "Medium", "High"];
const pdm = ["Completed", "In progress", "Pending", "N/A"];
const cycles = ["Cycle 1", "Cycle 2", "Cycle 3", "Cycle 4"];

const header = [
  "Transaction_ID", "Date", "Year", "Quarter", "Month", "Project_ID", "Project_Name", "Country", "Location", "Branch_or_Base",
  "Donor_ID", "Donor_Name", "Grant_ID", "Budget_Line_ID", "Budget_Category", "Budget_Line", "Approved_Budget", "Revised_Budget",
  "Actual_Expenditure", "Commitment", "Forecast_Expenditure", "Currency", "Activity", "Sector", "Modality", "Beneficiaries_Planned",
  "Beneficiaries_Reached", "Women", "Men", "Girls", "Boys", "Documentation_Status", "Procurement_Status", "Reporting_Status",
  "Audit_Risk_Level", "Compliance_Flag", "Comments", "Payment_Cycle", "Transfer_Value", "Households_Reached", "Total_Cash_Transferred",
  "PDM_Status", "Distribution_Branch", "Transfer_Modality", "Donor_Deadline_Risk"
];

const csv = (value) => `"${String(value).replaceAll('"', '""')}"`;
const rows = [header.join(",")];

for (let i = 1; i <= 540; i += 1) {
  const project = projects[(i - 1) % projects.length];
  const donor = donors[(i + 2) % donors.length];
  const line = budgetLines[(i + 4) % budgetLines.length];
  const date = new Date(Date.UTC(2024 + Math.floor((i - 1) / 216), (i - 1) % 12, 1 + ((i * 3) % 24)));
  const year = date.getUTCFullYear();
  const monthNumber = date.getUTCMonth() + 1;
  const quarter = `Q${Math.ceil(monthNumber / 3)}`;
  const month = date.toLocaleString("en-US", { month: "long", timeZone: "UTC" });
  const isCva = project[5] === "CVA" || line[1] === "CVA Transfers";
  const approved = 8500 + ((i * 1379) % 82000);
  const revised = Math.round(approved * (1 + (((i % 9) - 3) / 100)));
  const actual = Math.round(revised * (0.18 + ((i % 62) / 100)));
  const commitment = Math.round(revised * (0.03 + ((i % 13) / 100)));
  const forecast = Math.round(actual + commitment + revised * (0.08 + ((i % 17) / 100)));
  const planned = project[5] === "Health" || project[5] === "CVA" || project[5] === "WASH" ? 120 + ((i * 19) % 2800) : 0;
  const reached = planned ? Math.round(planned * (0.58 + ((i % 38) / 100))) : 0;
  const women = Math.round(reached * 0.34);
  const men = Math.round(reached * 0.27);
  const girls = Math.round(reached * 0.21);
  const boys = Math.max(0, reached - women - men - girls);
  const transferValue = isCva ? 80 + ((i % 8) * 15) : 0;
  const households = isCva ? Math.round(reached / 4.6) : 0;
  const totalCash = isCva ? transferValue * households : 0;
  const doc = docs[i % docs.length];
  const proc = procurement[i % procurement.length];
  const rep = reporting[i % reporting.length];
  const risk = risks[(doc === "Missing" || proc === "Gap identified" || rep === "Late") ? 3 : i % risks.length];
  const compliant = doc === "Complete" && proc === "Complete" && rep === "On time" ? "Compliant" : "Review";
  const deadline = rep === "Late" || risk === "High" ? "High" : risk === "Medium" ? "Medium" : "Low";
  const grant = `G-${donor[1].replaceAll(" ", "").slice(0, 4).toUpperCase()}-${project[0]}-${year}`;
  const activity = isCva ? "Cash assistance payment" : project[5] === "WASH" ? "WASH service delivery" : project[5] === "Health" ? "Health service support" : "Programme operations";

  rows.push([
    `TXN-SYN-${String(i).padStart(4, "0")}`, date.toISOString().slice(0, 10), year, quarter, month, project[0], project[1], project[2], project[3], project[4],
    donor[0], donor[1], grant, line[0], line[1], line[2], approved, revised, actual, commitment, forecast, donor[2], activity, project[5], project[6],
    planned, reached, women, men, girls, boys, doc, proc, rep, risk, compliant, "Synthetic anonymised portfolio record",
    isCva ? cycles[i % cycles.length] : "N/A", transferValue, households, totalCash, isCva ? pdm[i % 3] : "N/A", project[4], isCva ? (i % 2 ? "Mobile money" : "Prepaid card") : "N/A", deadline
  ].map(csv).join(","));
}

await mkdir(root, { recursive: true });
await writeFile(join(root, "humanitarian_finance_fact.csv"), rows.join("\n"), "utf8");
console.log(`Wrote ${rows.length - 1} synthetic transaction rows.`);
