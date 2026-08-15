"""Client-neutral resume structure that every parser produces and every
template renderer consumes."""

from dataclasses import dataclass, field, asdict


@dataclass
class Job:
    company: str = ""
    dates: str = ""
    title: str = ""
    project: str = ""
    bullets: list[str] = field(default_factory=list)


@dataclass
class Education:
    degree: str = ""
    institution: str = ""
    year: str = ""


@dataclass
class SkillGroup:
    category: str = ""
    values: str = ""


@dataclass
class ResumeData:
    name: str = ""
    summary: list[str] = field(default_factory=list)
    skills: list[SkillGroup] = field(default_factory=list)
    experience: list[Job] = field(default_factory=list)
    certifications: list[str] = field(default_factory=list)
    education: list[Education] = field(default_factory=list)
    # Sections the client format has no home for; surfaced as a review warning
    # so the recruiter decides whether anything needs manual carry-over.
    dropped_sections: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return asdict(self)

    @classmethod
    def from_dict(cls, d: dict) -> "ResumeData":
        return cls(
            name=d.get("name", ""),
            summary=list(d.get("summary", [])),
            skills=[SkillGroup(**s) for s in d.get("skills", [])],
            experience=[Job(**j) for j in d.get("experience", [])],
            certifications=list(d.get("certifications", [])),
            education=[Education(**e) for e in d.get("education", [])],
            dropped_sections=list(d.get("dropped_sections", [])),
        )
