from dataclasses import dataclass


@dataclass
class SocialAgent:
    name: str
    mode: str = "idle"

    def step(self, observation: str) -> str:
        return f"{self.name}/{self.mode}: ack:{observation[:80]}"
