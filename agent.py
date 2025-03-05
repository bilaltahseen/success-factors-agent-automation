from langchain_openai import ChatOpenAI

from browser_use import Agent, Controller
from browser_use.browser.browser import Browser, BrowserConfig
from browser_use.browser.context import BrowserContext, BrowserContextConfig
from browser_use.agent.views import ActionResult
import asyncio
import tasks
from dotenv import load_dotenv

load_dotenv()


browser_context_config = BrowserContextConfig(
    viewport_expansion=-1,
    no_viewport=False,  # Ensure viewport is enabled
    trace_path="./tmp/traces/",
)


# Configure the browser to connect to your Chrome instance
browser = Browser(
    config=BrowserConfig(
        chrome_instance_path="C:/Program Files/Google/Chrome/Application/chrome.exe",
        new_context_config=browser_context_config,  # Apply viewport settings here
    )
)


controller = Controller()


@controller.registry.action("click using querySelector")
async def click_element(browser: BrowserContext, selector: str):
    page = await browser.get_current_page()

    # Wait for the element to be visible
    await page.wait_for_selector(selector, state="visible")

    # Click the element
    await page.click(selector)

    return ActionResult(success=True, message=f"Clicked on element: {selector}")


@controller.registry.action("take screenshot")
async def take_screenshot(browser: BrowserContext, file_name: str):
    page = await browser.get_current_page()

    # Take a screenshot
    await page.screenshot(path=file_name,full_page=True)

    return ActionResult(success=True, message=f"Screenshot saved as: {file_name}")

async def run_agent_with_fresh_context(task: str):
    llm = ChatOpenAI(model="gpt-4o", temperature=0.0)

    async with await browser.new_context() as context:

        agent = Agent(
            task=task,
            llm=llm,
            browser_context=context,
            controller=controller,
        )

        # Run agent and log steps
        print("Starting Agent Execution")
        await agent.run(max_steps=50)
        result = agent.history.final_result()
        print("Final Result:", result)
        return result


result = asyncio.run(run_agent_with_fresh_context(task=tasks.case_1))
print("Execution Finished:", result)
