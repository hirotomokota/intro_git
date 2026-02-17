import os

from crewai import Agent, Crew, Process, Task

os.environ["ANTHROPIC_API_KEY"] = "sk-ant-xxxxxxxxxxxxxxxx"

# --- Agents ---

researcher = Agent(
    role="Researcher",
    goal="AI市場の最新トレンドと主要プレイヤーを調査する",
    backstory=(
        "あなたはテクノロジー業界に精通した市場調査の専門家です。"
        "公開情報から的確にトレンドを読み取り、簡潔にまとめる能力があります。"
    ),
    llm="anthropic/claude-sonnet-4-5-20250929",
    verbose=True,
)

analyst = Agent(
    role="Analyst",
    goal="競合他社の財務データを分析し、強み・弱みを明らかにする",
    backstory=(
        "あなたは財務分析のプロフェッショナルです。"
        "数字の裏にあるビジネスインサイトを見抜く力に定評があります。"
    ),
    llm="anthropic/claude-sonnet-4-5-20250929",
    verbose=True,
)

summarizer = Agent(
    role="Summarizer",
    goal="調査・分析結果を統合し、経営層向けの最終レポートを作成する",
    backstory=(
        "あなたは戦略コンサルタントとして数多くのレポートを手がけてきました。"
        "複数の情報源を一つのストーリーにまとめ上げることが得意です。"
    ),
    llm="anthropic/claude-sonnet-4-5-20250929",
    verbose=True,
)

# --- Tasks ---

research_task = Task(
    description=(
        "2024〜2025年のAI市場における主要トレンドを調査してください。"
        "特に生成AI、エッジAI、AI規制の動向に注目し、"
        "主要プレイヤー（OpenAI、Google、Meta、Anthropicなど）の戦略をまとめてください。"
    ),
    expected_output=(
        "AI市場の主要トレンド3〜5項目と、各主要プレイヤーの戦略概要を含む調査レポート"
    ),
    agent=researcher,
)

analysis_task = Task(
    description=(
        "調査結果をもとに、主要AI企業の競争力を分析してください。"
        "各社の強み・弱み・市場ポジションを評価し、"
        "今後の成長可能性についてインサイトを提供してください。"
    ),
    expected_output=(
        "主要AI企業ごとの強み・弱み分析と、市場ポジションの評価レポート"
    ),
    agent=analyst,
)

summary_task = Task(
    description=(
        "調査と分析の結果を統合し、経営層が意思決定に使える最終レポートを作成してください。"
        "エグゼクティブサマリー、主要な発見事項、推奨アクションを含めてください。"
    ),
    expected_output=(
        "エグゼクティブサマリー、主要発見事項、推奨アクションを含む"
        "A4で2〜3ページ相当の最終レポート"
    ),
    agent=summarizer,
)

# --- Crew ---

crew = Crew(
    agents=[researcher, analyst, summarizer],
    tasks=[research_task, analysis_task, summary_task],
    process=Process.sequential,
    verbose=True,
)

if __name__ == "__main__":
    result = crew.kickoff()
    print("=" * 60)
    print("最終レポート")
    print("=" * 60)
    print(result)
