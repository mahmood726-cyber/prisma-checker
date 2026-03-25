"""
PRISMA 2020 Compliance Checker — Selenium Test Suite
25 tests covering all 4 tabs, checklist items, dashboard, extensions, export.
Run: python test_prisma_checker.py
"""
import sys, os, time, io, unittest
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

HTML_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'prisma-checker.html')
URL = 'file:///' + HTML_PATH.replace('\\', '/')


def get_driver():
    opts = Options()
    opts.add_argument('--headless=new')
    opts.add_argument('--no-sandbox')
    opts.add_argument('--disable-gpu')
    opts.add_argument('--window-size=1400,900')
    opts.set_capability('goog:loggingPrefs', {'browser': 'ALL'})
    driver = webdriver.Chrome(options=opts)
    driver.implicitly_wait(2)
    return driver


class PRISMACheckerTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = get_driver()
        cls.driver.get(URL)
        cls.driver.execute_script("try{localStorage.removeItem('prismachecker-data')}catch(e){}")
        cls.driver.get(URL)
        time.sleep(0.5)

    @classmethod
    def tearDownClass(cls):
        logs = cls.driver.get_log('browser')
        severe = [l for l in logs if l['level'] == 'SEVERE' and 'favicon' not in l.get('message', '')]
        if severe:
            print(f"\nJS ERRORS ({len(severe)}):")
            for l in severe:
                print(f"  {l['message']}")
        cls.driver.quit()

    def _reload(self):
        self.driver.execute_script("try{localStorage.removeItem('prismachecker-data')}catch(e){}")
        self.driver.get(URL)
        time.sleep(0.5)

    def _click(self, by, val):
        el = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located((by, val)))
        self.driver.execute_script("arguments[0].click()", el)
        return el

    # ─── 1. PAGE LOAD ───
    def test_01_page_loads(self):
        """Page loads with correct title."""
        self.assertIn('PRISMA', self.driver.title)

    def test_02_hero_visible(self):
        """Hero/header area is visible."""
        header = self.driver.find_element(By.CSS_SELECTOR, 'header, .hero, h1')
        self.assertTrue(header.is_displayed())

    def test_03_four_tabs(self):
        """All 4 tabs exist."""
        tabs = self.driver.find_elements(By.CSS_SELECTOR, '.tab-btn')
        self.assertEqual(len(tabs), 4)

    def test_04_checklist_tab_active(self):
        """Checklist tab is active by default."""
        tab = self.driver.find_element(By.ID, 'tab-checklist')
        self.assertEqual(tab.get_attribute('aria-selected'), 'true')

    # ─── 2. CHECKLIST ITEMS ───
    def test_05_checklist_items_exist(self):
        """At least 27 checklist items are rendered."""
        self._reload()
        items = self.driver.find_elements(By.CSS_SELECTOR, '.checklist-item')
        self.assertGreaterEqual(len(items), 27)

    def test_06_sections_present(self):
        """Checklist sections are grouped (Title, Abstract, Introduction, etc.)."""
        self._reload()
        sections = self.driver.find_elements(By.CSS_SELECTOR, '.section-header')
        self.assertGreaterEqual(len(sections), 6)  # Title, Abstract, Intro, Methods, Results, Discussion, Other

    def test_07_status_radios(self):
        """Each item has status radio buttons."""
        self._reload()
        # Find item 1's radios by ID pattern
        radios = self.driver.find_elements(By.CSS_SELECTOR, '#item-card-1 input[type="radio"]')
        if len(radios) == 0:
            # Radios might be outside the card — try by name pattern
            radios = self.driver.find_elements(By.CSS_SELECTOR, 'input[id^="status-1-"]')
        self.assertGreaterEqual(len(radios), 3)  # Reported, Partially, Not reported, N/A

    def test_08_set_item_reported(self):
        """Setting an item to 'Reported' updates its visual status."""
        self._reload()
        # Click the first "Reported" radio
        reported_radio = self.driver.find_element(By.ID, 'status-1-reported')
        self.driver.execute_script("arguments[0].click()", reported_radio)
        time.sleep(0.3)
        # The item card should reflect the status
        card = self.driver.find_element(By.ID, 'item-card-1')
        status = card.get_attribute('data-status')
        self.assertEqual(status, 'reported')

    def test_09_set_item_not_reported(self):
        """Setting an item to 'Not reported' updates its status."""
        self._reload()
        not_reported = self.driver.find_element(By.ID, 'status-1-not-reported')
        self.driver.execute_script("arguments[0].click()", not_reported)
        time.sleep(0.3)
        card = self.driver.find_element(By.ID, 'item-card-1')
        self.assertEqual(card.get_attribute('data-status'), 'not-reported')

    def test_10_page_reference_input(self):
        """Page reference input accepts text."""
        self._reload()
        page_input = self.driver.find_element(By.ID, 'page-1')
        page_input.send_keys('p.3, Methods')
        self.assertEqual(page_input.get_attribute('value'), 'p.3, Methods')

    def test_11_notes_textarea(self):
        """Notes textarea accepts text."""
        self._reload()
        notes = self.driver.find_element(By.ID, 'notes-1')
        notes.send_keys('Title clearly identifies this as a systematic review')
        self.assertIn('systematic review', notes.get_attribute('value'))

    # ─── 3. TAB NAVIGATION ───
    def test_12_tab_click_navigation(self):
        """Clicking dashboard tab switches panels."""
        self._click(By.ID, 'tab-dashboard')
        time.sleep(0.3)
        panel = self.driver.find_element(By.ID, 'panel-dashboard')
        self.assertIn('active', panel.get_attribute('class'))

    def test_13_tab_keyboard_navigation(self):
        """Arrow keys navigate tabs."""
        self._reload()
        tab = self.driver.find_element(By.ID, 'tab-checklist')
        tab.send_keys(Keys.ARROW_RIGHT)
        time.sleep(0.2)
        dash_tab = self.driver.find_element(By.ID, 'tab-dashboard')
        self.assertEqual(dash_tab.get_attribute('aria-selected'), 'true')

    # ─── 4. DASHBOARD ───
    def test_14_dashboard_renders(self):
        """Dashboard tab shows content."""
        self._reload()
        # Set a few items first
        self.driver.execute_script("arguments[0].click()", self.driver.find_element(By.ID, 'status-1-reported'))
        self.driver.execute_script("arguments[0].click()", self.driver.find_element(By.ID, 'status-2-reported'))
        time.sleep(0.2)
        self._click(By.ID, 'tab-dashboard')
        time.sleep(0.3)
        container = self.driver.find_element(By.ID, 'dashboardContainer')
        self.assertTrue(len(container.text) > 0)

    def test_15_compliance_score(self):
        """Dashboard shows a compliance score."""
        self._reload()
        self.driver.execute_script("arguments[0].click()", self.driver.find_element(By.ID, 'status-1-reported'))
        time.sleep(0.2)
        self._click(By.ID, 'tab-dashboard')
        time.sleep(0.3)
        text = self.driver.find_element(By.ID, 'dashboardContainer').text
        self.assertTrue('%' in text or 'compliance' in text.lower() or 'score' in text.lower())

    def test_16_compliance_statement(self):
        """Dashboard generates a compliance statement."""
        # Continuing from previous state
        container = self.driver.find_element(By.ID, 'dashboardContainer')
        statement = container.find_elements(By.CSS_SELECTOR, '.compliance-statement')
        self.assertGreater(len(statement), 0)

    # ─── 5. DARK MODE ───
    def test_17_theme_toggle(self):
        """Theme toggle switches between dark and light."""
        self._reload()
        btn = self.driver.find_element(By.ID, 'themeToggle')
        initial = self.driver.find_element(By.TAG_NAME, 'html').get_attribute('data-theme')
        self.driver.execute_script("arguments[0].click()", btn)
        time.sleep(0.2)
        toggled = self.driver.find_element(By.TAG_NAME, 'html').get_attribute('data-theme')
        self.assertNotEqual(initial, toggled)
        # Toggle back
        self.driver.execute_script("arguments[0].click()", btn)

    # ─── 6. EXTENSIONS ───
    def test_18_extensions_tab(self):
        """Extensions tab shows extension options."""
        self._click(By.ID, 'tab-extensions')
        time.sleep(0.3)
        container = self.driver.find_element(By.ID, 'extensionsContainer')
        self.assertTrue(container.is_displayed())
        text = container.text.lower()
        self.assertTrue('prisma' in text)

    def test_19_extension_checkboxes(self):
        """Extension cards have checkboxes."""
        self._click(By.ID, 'tab-extensions')
        time.sleep(0.3)
        checkboxes = self.driver.find_elements(By.CSS_SELECTOR, '.extension-check')
        self.assertGreater(len(checkboxes), 0)

    # ─── 7. EXPORT ───
    def test_20_export_tab(self):
        """Export tab shows export options."""
        self._click(By.ID, 'tab-export')
        time.sleep(0.3)
        container = self.driver.find_element(By.ID, 'exportContainer')
        self.assertTrue(container.is_displayed())

    def test_21_export_csv_button(self):
        """CSV export button exists."""
        self._click(By.ID, 'tab-export')
        time.sleep(0.2)
        csv_btn = self.driver.find_element(By.ID, 'exportCSV')
        self.assertTrue(csv_btn.is_displayed())

    def test_22_export_json_button(self):
        """JSON export button exists."""
        json_btn = self.driver.find_element(By.ID, 'exportJSON')
        self.assertTrue(json_btn.is_displayed())

    def test_23_export_clipboard_button(self):
        """Clipboard copy button exists."""
        clip_btn = self.driver.find_element(By.ID, 'exportClipboard')
        self.assertTrue(clip_btn.is_displayed())

    # ─── 8. EXPAND/RESET ───
    def test_24_expand_all(self):
        """Expand All button exists and is clickable."""
        self._click(By.ID, 'tab-checklist')
        time.sleep(0.2)
        btn = self.driver.find_element(By.ID, 'btnExpandAll')
        self.assertTrue(btn.is_displayed())

    def test_25_reset_all(self):
        """Reset All button clears assessments."""
        self._reload()
        # Set an item
        self.driver.execute_script("arguments[0].click()", self.driver.find_element(By.ID, 'status-1-reported'))
        time.sleep(0.2)
        card = self.driver.find_element(By.ID, 'item-card-1')
        self.assertEqual(card.get_attribute('data-status'), 'reported')
        # Reset
        self._click(By.ID, 'btnResetAll')
        time.sleep(0.5)
        # Accept any confirmation dialog
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
            time.sleep(0.3)
        except Exception:
            pass
        card = self.driver.find_element(By.ID, 'item-card-1')
        status = card.get_attribute('data-status')
        self.assertTrue(status == '' or status is None or status == 'null')


if __name__ == '__main__':
    unittest.main(verbosity=2)
