case_1 = """

### Task: Execute Steps Exactly as Defined

#### **Rules (Do NOT Deviate)**
- Do **NOT** assume missing details or optimize the steps.
- Do **NOT** change the order or skip any step.
- Execute **ONLY** what is written. If something is unclear, **STOP**.
- **Wait for elements to be ready** before interacting.
- If an action fails, **retry up to 10 times** then **move to the next step**.

#### **Steps:**
1. Open [SAP SuccessFactors Login](https://hcm-us10-sales.hr.cloud.sap/login?company=<company>).
2. Enter **Username:** `<username>` and **Password:** `<password>`.
3. Wait for the page to fully load before continuing.
4. Open **Manage Permission Roles**.
5. Click `[data-testid="rbpCreateRoleButton"]` using `querySelector`. Do not search for the **Create** button.
6. Set role details:
   - **Name:** `Demo Role`
   - **User Type:** `Employee` (if not already selected).
7. Click `[data-testid="wizard-next"]` using `querySelector`.
8. Search for **Employee Views** and press `Enter`.
9. Scroll to each checkbox and click it using the following process (**Do not retry** if a checkbox fails):
   - Locate the checkbox using `querySelector`:  
     **div[role=row]:has(div[aria-label="{label} "]) ui5-checkbox**  
     where `{label}` is one of:
     - **"Benefits", "Drivers License", "Employment", "Time", and "Time Off"**
   - **Ensure it is loaded** before interacting.
   - **Scroll to it** using `scrollIntoView({ behavior: "smooth", block: "center" })`.
   - **Wait briefly** for stability before clicking.
   - **Click the checkbox** once it is visible.
10. Click `[data-testid="wizard-next"]` using `querySelector`.
11. Take a screenshot of current page using "take_screenshot" action with filename `demo_role.png`.
12. Click `[data-testid="wizard-save"]` using `querySelector`.
13. Wait for the **Success** message to appear then click `[data-action="Yes"]` using `querySelector`.
14. Set role assignment details:
   - **Name:** `All HR Managers`
15. Locate the next button and click it, always use **[data-testid="wizard-next"]*** as the selector.
16. Open the dropdown for **Grant Access To** using `[data-testid=add-assignment-relation-role-select]` `querySelector` and perform the following steps:
   - Press down arrow key after clicking the dropdown.
   - Press `Enter` to select **HR Managers**.
17. Click `[data-testid="wizard-next"]` using `querySelector` until you reach the **Preview** step then click `[data-testid="wizard-save"]` using `querySelector`.
20. Take a screenshot of current page using "take_screenshot" action with filename `role_assignment.png`.

#### **Critical Constraints**
- **DO NOT** take actions not listed above.
- **DO NOT** proceed if a step is missing or unclear.
- **DO NOT** assume page structure; always wait for elements before interacting.

### **Final Check**
- Verify all steps completed exactly as written.
- Output `SUCCESS` or `FAILED` with reasons.

"""
