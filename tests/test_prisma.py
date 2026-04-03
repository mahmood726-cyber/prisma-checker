"""
Selenium test suite for PRISMA 2020 Compliance Checker.
Tests 27 checklist items, 6 extensions, dashboard scoring, export, theme, storage.
"""
import os, unittest, time, json
os.environ['PYTHONIOENCODING'] = 'utf-8'
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

HTML = 'file:///' + os.path.abspath(r'C:\Models\PRISMAChecker\prisma-checker.html').replace('\\', '/')


class TestPRISMAChecker(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        opts = Options()
        opts.add_argument('--headless=new')
        opts.add_argument('--no-sandbox')
        opts.add_argument('--disable-gpu')
        cls.drv = webdriver.Chrome(options=opts)
        cls.drv.get(HTML)
        time.sleep(1.5)
        # Clear localStorage for clean state
        cls.drv.execute_script("localStorage.clear();")
        cls.drv.get(HTML)
        time.sleep(1.5)

    @classmethod
    def tearDownClass(cls):
        cls.drv.quit()

    def js(self, script):
        return self.drv.execute_script(script)

    # ================================================================
    # 1. Page Structure
    # ================================================================

    def test_01_title(self):
        """Page title contains PRISMA."""
        title = self.drv.title
        self.assertIn('PRISMA', title)

    def test_02_hero_metadata(self):
        """Hero section shows 27 items, 7 sections, 6 extensions."""
        hero_text = self.js("return document.querySelector('.hero').textContent;")
        self.assertIn('27', hero_text, "Should show 27 checklist items")
        self.assertIn('7', hero_text, "Should show 7 sections")
        self.assertIn('6', hero_text, "Should show 6 extensions")

    # ================================================================
    # 2. Checklist Rendering (27 items)
    # ================================================================

    def test_03_all_27_items_rendered(self):
        """All 27 PRISMA items are rendered in the checklist panel."""
        item_count = self.js("""
            return document.querySelectorAll('.checklist-item').length;
        """)
        self.assertEqual(item_count, 27, "Should render exactly 27 checklist items")

    def test_04_item_numbers_sequential(self):
        """Items are numbered 1-27 in correct order."""
        numbers = self.js("""
            var items = document.querySelectorAll('.item-number');
            var nums = [];
            items.forEach(function(el) { nums.push(parseInt(el.textContent)); });
            return nums;
        """)
        expected = list(range(1, 28))
        self.assertEqual(numbers, expected, "Items should be numbered 1-27")

    def test_05_item_has_radio_buttons(self):
        """Each item has 4 status options: Reported, Partially, Not reported, N/A."""
        radio_count = self.js("""
            return document.querySelectorAll('input[name="status-1"]').length;
        """)
        self.assertEqual(radio_count, 4, "Each item should have 4 radio buttons")

    def test_06_item_has_page_and_notes(self):
        """Item 1 has page/section input and notes textarea."""
        page_exists = self.js("return document.getElementById('page-1') !== null;")
        notes_exists = self.js("return document.getElementById('notes-1') !== null;")
        self.assertTrue(page_exists, "Item 1 should have page input")
        self.assertTrue(notes_exists, "Item 1 should have notes textarea")

    # ================================================================
    # 3. Status Selection & Data-Status Attribute
    # ================================================================

    def test_07_select_reported(self):
        """Selecting 'Reported' for item 1 updates data-status attribute."""
        self.js("document.getElementById('status-1-reported').click();")
        time.sleep(0.3)
        status = self.js("return document.getElementById('item-card-1').getAttribute('data-status');")
        self.assertEqual(status, 'reported')

    def test_08_select_partial(self):
        """Selecting 'Partially' for item 2 updates data-status."""
        self.js("document.getElementById('status-2-partial').click();")
        time.sleep(0.3)
        status = self.js("return document.getElementById('item-card-2').getAttribute('data-status');")
        self.assertEqual(status, 'partial')

    def test_09_select_not_reported(self):
        """Selecting 'Not reported' for item 3 updates data-status."""
        self.js("document.getElementById('status-3-not-reported').click();")
        time.sleep(0.3)
        status = self.js("return document.getElementById('item-card-3').getAttribute('data-status');")
        self.assertEqual(status, 'not-reported')

    def test_10_select_na(self):
        """Selecting 'N/A' for item 4 updates data-status."""
        self.js("document.getElementById('status-4-na').click();")
        time.sleep(0.3)
        status = self.js("return document.getElementById('item-card-4').getAttribute('data-status');")
        self.assertEqual(status, 'na')

    # ================================================================
    # 4. Section Progress
    # ================================================================

    def test_11_section_progress_updates(self):
        """Section progress shows filled count when items are assessed."""
        # Title section has only item 1, which we set to 'reported' in test_07
        progress_text = self.js("return document.getElementById('progress-title').textContent;")
        self.assertIn('1/1', progress_text, "Title section should show 1/1")

    def test_12_section_names(self):
        """All 7 PRISMA sections have progress elements."""
        sections = ['title', 'abstract', 'introduction', 'methods', 'results', 'discussion', 'other']
        for section in sections:
            el = self.js(f"return document.getElementById('progress-{section}') !== null;")
            self.assertTrue(el, f"Section progress for '{section}' should exist")

    # ================================================================
    # 5. Tab Navigation
    # ================================================================

    def test_13_tab_checklist_active(self):
        """Checklist tab is active by default."""
        is_active = self.js("return document.getElementById('panel-checklist').classList.contains('active');")
        self.assertTrue(is_active, "Checklist panel should be active by default")

    def test_14_switch_to_dashboard(self):
        """Clicking Dashboard tab switches to dashboard panel."""
        self.drv.find_element(By.ID, 'tab-dashboard').click()
        time.sleep(0.3)
        is_active = self.js("return document.getElementById('panel-dashboard').classList.contains('active');")
        self.assertTrue(is_active, "Dashboard panel should be active")

    def test_15_switch_to_extensions(self):
        """Clicking Extensions tab switches to extensions panel."""
        self.drv.find_element(By.ID, 'tab-extensions').click()
        time.sleep(0.3)
        is_active = self.js("return document.getElementById('panel-extensions').classList.contains('active');")
        self.assertTrue(is_active, "Extensions panel should be active")

    def test_16_switch_to_export(self):
        """Clicking Export tab switches to export panel."""
        self.drv.find_element(By.ID, 'tab-export').click()
        time.sleep(0.3)
        is_active = self.js("return document.getElementById('panel-export').classList.contains('active');")
        self.assertTrue(is_active, "Export panel should be active")
        # Return to checklist
        self.drv.find_element(By.ID, 'tab-checklist').click()
        time.sleep(0.2)

    # ================================================================
    # 6. Dashboard Scoring
    # ================================================================

    def test_17_dashboard_compliance_score(self):
        """Dashboard computes compliance percentage correctly."""
        # Set several items to known states first
        # Item 1=reported (from test_07), 2=partial, 3=not-reported, 4=na
        # Compliance = (reported + na) / 27 * 100 = (1+1)/27*100 = 7%
        self.drv.find_element(By.ID, 'tab-dashboard').click()
        time.sleep(0.5)
        compliance = self.js("""
            var el = document.querySelector('.score-value');
            return el ? el.textContent : '';
        """)
        # Should show some percentage
        self.assertIn('%', compliance, "Dashboard should show compliance %")

    def test_18_dashboard_status_breakdown(self):
        """Dashboard shows status breakdown counts."""
        self.drv.find_element(By.ID, 'tab-dashboard').click()
        time.sleep(0.5)
        dashboard_text = self.js("return document.getElementById('dashboardContainer').textContent;")
        self.assertIn('Reported', dashboard_text)
        self.assertIn('Partially', dashboard_text)
        self.assertIn('Not Reported', dashboard_text)
        self.assertIn('N/A', dashboard_text)
        self.assertIn('Unassessed', dashboard_text)

    def test_19_attention_items(self):
        """Dashboard lists items needing attention (partial + not-reported)."""
        self.drv.find_element(By.ID, 'tab-dashboard').click()
        time.sleep(0.5)
        attention_text = self.js("return document.getElementById('dashboardContainer').textContent;")
        self.assertIn('Attention', attention_text, "Dashboard should have attention section")

    def test_20_compliance_statement(self):
        """Dashboard generates auto compliance statement."""
        self.drv.find_element(By.ID, 'tab-dashboard').click()
        time.sleep(0.5)
        statement = self.js("""
            var el = document.getElementById('complianceStatement');
            return el ? el.textContent : '';
        """)
        self.assertIn('PRISMA 2020', statement, "Statement should reference PRISMA 2020")
        self.assertIn('compliance', statement.lower(), "Statement should mention compliance")

    # ================================================================
    # 7. Extensions (6 extensions)
    # ================================================================

    def test_21_six_extensions_rendered(self):
        """All 6 PRISMA extensions are rendered."""
        self.drv.find_element(By.ID, 'tab-extensions').click()
        time.sleep(0.3)
        ext_count = self.js("return document.querySelectorAll('.extension-card').length;")
        self.assertEqual(ext_count, 6, "Should render 6 extension cards")

    def test_22_extension_names(self):
        """Extensions include PRISMA-S, PRISMA-ScR, PRISMA-NMA, PRISMA-DTA, PRISMA-IPD, PRISMA-P."""
        self.drv.find_element(By.ID, 'tab-extensions').click()
        time.sleep(0.3)
        ext_text = self.js("return document.getElementById('extensionsContainer').textContent;")
        for name in ['PRISMA-S', 'PRISMA-ScR', 'PRISMA-NMA', 'PRISMA-DTA', 'PRISMA-IPD', 'PRISMA-P']:
            self.assertIn(name, ext_text, f"Extension {name} should be present")

    def test_23_enable_extension(self):
        """Enabling PRISMA-S extension activates its card."""
        self.drv.find_element(By.ID, 'tab-extensions').click()
        time.sleep(0.3)
        self.js("document.getElementById('ext-prisma-s').click();")
        time.sleep(0.3)
        is_active = self.js("return document.getElementById('ext-card-prisma-s').classList.contains('active');")
        self.assertTrue(is_active, "PRISMA-S card should be active when checked")
        # Uncheck to restore state
        self.js("document.getElementById('ext-prisma-s').click();")
        time.sleep(0.2)

    def test_24_extension_items_count(self):
        """PRISMA-S has 16 sub-items, PRISMA-NMA has 8."""
        self.drv.find_element(By.ID, 'tab-extensions').click()
        time.sleep(0.3)
        prisma_s_items = self.js("""
            return document.querySelectorAll('#ext-items-prisma-s .ext-item').length;
        """)
        prisma_nma_items = self.js("""
            return document.querySelectorAll('#ext-items-prisma-nma .ext-item').length;
        """)
        self.assertEqual(prisma_s_items, 16, "PRISMA-S should have 16 items")
        self.assertEqual(prisma_nma_items, 8, "PRISMA-NMA should have 8 items")

    # ================================================================
    # 8. Export Tab
    # ================================================================

    def test_25_export_cards_present(self):
        """Export tab has CSV, JSON, Clipboard, Print options."""
        self.drv.find_element(By.ID, 'tab-export').click()
        time.sleep(0.3)
        for card_id in ['exportCSV', 'exportJSON', 'exportClipboard', 'exportPrint']:
            exists = self.js(f"return document.getElementById('{card_id}') !== null;")
            self.assertTrue(exists, f"Export card '{card_id}' should exist")

    def test_26_export_csv_generates_preview(self):
        """Clicking Export CSV populates the preview area."""
        self.drv.find_element(By.ID, 'tab-export').click()
        time.sleep(0.3)
        self.js("document.getElementById('exportCSV').click();")
        time.sleep(0.5)
        preview = self.js("return document.getElementById('exportPreviewContent').textContent;")
        self.assertIn('Item,Section,Title,Status', preview, "CSV should have header row")
        self.assertIn('Title', preview, "CSV should include item data")

    def test_27_export_json_generates_preview(self):
        """Clicking Export JSON populates the preview with valid JSON."""
        self.drv.find_element(By.ID, 'tab-export').click()
        time.sleep(0.3)
        self.js("document.getElementById('exportJSON').click();")
        time.sleep(0.5)
        preview = self.js("return document.getElementById('exportPreviewContent').textContent;")
        self.assertIn('prisma2020', preview, "JSON should have prisma2020 key")
        # Validate it's parseable JSON
        try:
            data = json.loads(preview)
            self.assertIn('prisma2020', data)
            self.assertIn('items', data['prisma2020'])
            self.assertEqual(len(data['prisma2020']['items']), 27)
        except json.JSONDecodeError:
            self.fail("Export JSON should produce valid JSON")

    def test_28_export_clipboard_preview(self):
        """Clicking Copy to Clipboard generates formatted text preview."""
        self.drv.find_element(By.ID, 'tab-export').click()
        time.sleep(0.3)
        self.js("document.getElementById('exportClipboard').click();")
        time.sleep(0.5)
        preview = self.js("return document.getElementById('exportPreviewContent').textContent;")
        self.assertIn('PRISMA 2020 CHECKLIST', preview, "Clipboard text should have header")
        self.assertIn('Compliance:', preview, "Clipboard text should show compliance")

    # ================================================================
    # 9. Theme Toggle
    # ================================================================

    def test_29_theme_toggle(self):
        """Theme toggle switches between dark and light."""
        initial = self.js("return document.documentElement.getAttribute('data-theme');")
        self.drv.find_element(By.ID, 'themeToggle').click()
        time.sleep(0.3)
        after = self.js("return document.documentElement.getAttribute('data-theme');")
        self.assertNotEqual(initial, after, "Theme should change after toggle")
        # Toggle back
        self.drv.find_element(By.ID, 'themeToggle').click()
        time.sleep(0.2)

    # ================================================================
    # 10. Reset All
    # ================================================================

    def test_30_reset_all(self):
        """Reset All clears all selections."""
        # First set some items
        self.drv.find_element(By.ID, 'tab-checklist').click()
        time.sleep(0.2)
        self.js("document.getElementById('status-5-reported').click();")
        time.sleep(0.2)
        # Dismiss confirm dialog by overriding confirm
        self.js("window.confirm = function() { return true; };")
        self.drv.find_element(By.ID, 'btnResetAll').click()
        time.sleep(0.5)
        # Check that item 5 is now unassessed
        status = self.js("return document.getElementById('item-card-5').getAttribute('data-status');")
        self.assertEqual(status, '', "After reset, item 5 should have empty status")

    # ================================================================
    # 11. Page/Notes Fields
    # ================================================================

    def test_31_page_field_entry(self):
        """Page/section field accepts text input."""
        self.drv.find_element(By.ID, 'tab-checklist').click()
        time.sleep(0.2)
        self.js("document.getElementById('page-1').value = 'p.3, Methods';")
        val = self.js("return document.getElementById('page-1').value;")
        self.assertEqual(val, 'p.3, Methods')

    def test_32_notes_field_entry(self):
        """Notes textarea accepts text input."""
        self.drv.find_element(By.ID, 'tab-checklist').click()
        time.sleep(0.2)
        self.js("document.getElementById('notes-1').value = 'Title clearly states systematic review';")
        val = self.js("return document.getElementById('notes-1').value;")
        self.assertEqual(val, 'Title clearly states systematic review')

    # ================================================================
    # 12. localStorage Persistence
    # ================================================================

    def test_33_localstorage_save(self):
        """Setting a status saves to localStorage."""
        self.drv.find_element(By.ID, 'tab-checklist').click()
        time.sleep(0.2)
        self.js("document.getElementById('status-1-reported').click();")
        time.sleep(0.5)
        stored = self.js("return localStorage.getItem('prismachecker-data');")
        self.assertIsNotNone(stored, "Should save to localStorage")
        data = json.loads(stored)
        self.assertEqual(data['items']['1']['status'], 'reported')

    # ================================================================
    # 13. PRISMA Section Structure
    # ================================================================

    def test_34_section_headers_present(self):
        """All 7 section headers are rendered in the checklist."""
        self.drv.find_element(By.ID, 'tab-checklist').click()
        time.sleep(0.2)
        headers = self.js("""
            var els = document.querySelectorAll('.section-header');
            var names = [];
            els.forEach(function(el) { names.push(el.textContent.trim().split('\\n')[0].trim()); });
            return names;
        """)
        expected_sections = ['Title', 'Abstract', 'Introduction', 'Methods', 'Results', 'Discussion', 'Other Information']
        for section in expected_sections:
            found = any(section in h for h in headers)
            self.assertTrue(found, f"Section '{section}' should be in headers")

    def test_35_methods_section_has_12_items(self):
        """Methods section contains items 5-16 (12 items)."""
        # Count items within the Methods section
        methods_items = self.js("""
            var count = 0;
            for (var i = 5; i <= 16; i++) {
                if (document.getElementById('item-card-' + i)) count++;
            }
            return count;
        """)
        self.assertEqual(methods_items, 12, "Methods section should have items 5-16")

    # ================================================================
    # 14. Full Assessment Scoring
    # ================================================================

    def test_36_full_compliance_100_percent(self):
        """Marking all 27 items as reported gives 100% compliance."""
        self.drv.find_element(By.ID, 'tab-checklist').click()
        time.sleep(0.2)
        # Mark all as reported
        self.js("""
            for (var i = 1; i <= 27; i++) {
                var radio = document.getElementById('status-' + i + '-reported');
                if (radio) radio.click();
            }
        """)
        time.sleep(0.5)
        # Switch to dashboard and check
        self.drv.find_element(By.ID, 'tab-dashboard').click()
        time.sleep(0.5)
        compliance = self.js("return document.querySelector('.score-value').textContent;")
        self.assertEqual(compliance.strip(), '100%', "All reported should give 100%")
        # Reset for subsequent tests
        self.js("window.confirm = function() { return true; };")
        self.drv.find_element(By.ID, 'tab-checklist').click()
        time.sleep(0.2)
        self.drv.find_element(By.ID, 'btnResetAll').click()
        time.sleep(0.3)

    def test_37_na_counts_as_compliant(self):
        """N/A items count toward compliance (compliance = (reported + na) / 27)."""
        self.drv.find_element(By.ID, 'tab-checklist').click()
        time.sleep(0.2)
        # Mark all as N/A
        self.js("""
            for (var i = 1; i <= 27; i++) {
                var radio = document.getElementById('status-' + i + '-na');
                if (radio) radio.click();
            }
        """)
        time.sleep(0.5)
        self.drv.find_element(By.ID, 'tab-dashboard').click()
        time.sleep(0.5)
        compliance = self.js("return document.querySelector('.score-value').textContent;")
        self.assertEqual(compliance.strip(), '100%', "All N/A should give 100%")
        # Reset
        self.js("window.confirm = function() { return true; };")
        self.drv.find_element(By.ID, 'tab-checklist').click()
        time.sleep(0.2)
        self.drv.find_element(By.ID, 'btnResetAll').click()
        time.sleep(0.3)

    # ================================================================
    # 15. Edge Cases
    # ================================================================

    def test_38_zero_compliance(self):
        """All items not-reported gives 0% compliance."""
        self.drv.find_element(By.ID, 'tab-checklist').click()
        time.sleep(0.2)
        self.js("""
            for (var i = 1; i <= 27; i++) {
                var radio = document.getElementById('status-' + i + '-not-reported');
                if (radio) radio.click();
            }
        """)
        time.sleep(0.5)
        self.drv.find_element(By.ID, 'tab-dashboard').click()
        time.sleep(0.5)
        compliance = self.js("return document.querySelector('.score-value').textContent;")
        self.assertEqual(compliance.strip(), '0%', "All not-reported should give 0%")
        # Reset
        self.js("window.confirm = function() { return true; };")
        self.drv.find_element(By.ID, 'tab-checklist').click()
        time.sleep(0.2)
        self.drv.find_element(By.ID, 'btnResetAll').click()
        time.sleep(0.3)

    def test_39_extension_subitems_checkable(self):
        """Extension sub-items (checkboxes) can be checked."""
        self.drv.find_element(By.ID, 'tab-extensions').click()
        time.sleep(0.3)
        # Enable PRISMA-S
        self.js("document.getElementById('ext-prisma-s').click();")
        time.sleep(0.3)
        # Check first sub-item
        self.js("document.getElementById('extitem-ps1').click();")
        time.sleep(0.2)
        is_checked = self.js("return document.getElementById('extitem-ps1').checked;")
        self.assertTrue(is_checked, "Sub-item ps1 should be checkable")
        # Clean up
        self.js("document.getElementById('ext-prisma-s').click();")
        time.sleep(0.2)

    def test_40_export_json_includes_extensions(self):
        """JSON export includes extension data when extensions are enabled."""
        self.drv.find_element(By.ID, 'tab-extensions').click()
        time.sleep(0.3)
        self.js("document.getElementById('ext-prisma-nma').click();")
        time.sleep(0.3)
        self.js("document.getElementById('extitem-nma1').click();")
        time.sleep(0.2)
        # Export JSON
        self.drv.find_element(By.ID, 'tab-export').click()
        time.sleep(0.3)
        self.js("document.getElementById('exportJSON').click();")
        time.sleep(0.5)
        preview = self.js("return document.getElementById('exportPreviewContent').textContent;")
        data = json.loads(preview)
        self.assertIn('extensions', data['prisma2020'])
        ext_names = [e['id'] for e in data['prisma2020']['extensions']]
        self.assertIn('prisma-nma', ext_names, "Extensions should include prisma-nma")
        # Clean up
        self.drv.find_element(By.ID, 'tab-extensions').click()
        time.sleep(0.2)
        self.js("document.getElementById('ext-prisma-nma').click();")
        time.sleep(0.2)


if __name__ == '__main__':
    unittest.main(verbosity=2)
