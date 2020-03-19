from candidates.models import User
from candidates.models import CandidateProfile
from candidates.models import VerificationCode
from candidates.models import Degree
from candidates.models import EntryTest
from candidates.models.WizardSession import WizardSession
from candidates.models import PriorityDegree
from candidates.models import MeritList
from candidates.models.Rejection import Rejection

__all__ = ['User', 'VerificationCode','CandidateProfile', 'Degree', 'EntryTest','PriorityDegree','MeritList','WizardSession', 'Rejection']
