# 🏠 Host Onboarding

Professional onboarding flow for Airbnb hosts - **100% Legal**, no credentials required.

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## ✨ Features

- 🔍 **Search by Address**: Find Airbnb listings near any address
- ✅ **Ownership Verification**: Multiple methods to prove listing ownership
- 🔐 **No Credentials Required**: Works with public data only
- ⚡ **Async Support**: Built for high-performance applications

## 🚀 Quick Start

```bash
pip install git+https://github.com/rabi3laser/host-onboarding.git
```

```python
import asyncio
from apify_connector import ApifyConnector
from host_onboarding import OnboardingService, VerificationMethod

async def onboard_host():
    async with ApifyConnector(api_token="your_token") as connector:
        service = OnboardingService(connector)
        
        # 1. Start session
        session = await service.start_session(user_id="user_123")
        
        # 2. Search listings
        listings = await service.search_by_address(
            session_id=session.session_id,
            address="123 Rue de Paris, 75018 Paris"
        )
        
        # 3. Select listing
        await service.select_listing(
            session_id=session.session_id,
            listing_id=listings[0].listing_id
        )
        
        # 4. Start verification
        verification = await service.start_verification(
            session_id=session.session_id,
            method=VerificationMethod.TITLE_CODE
        )
        print(f"Add code to title: {verification['code']}")
        
        # 5. Verify
        result = await service.verify(session_id=session.session_id)
        if result.success:
            print("✅ Connected!")

asyncio.run(onboard_host())
```

## 🔐 Verification Methods

| Method | Reliability | Description |
|--------|-------------|-------------|
| **Title Code** ⭐ | High | Add unique code to listing title |
| **iCal URL** | Medium | Provide calendar export URL |
| **Screenshot** | Manual | Upload dashboard screenshot |

## 📋 Flow

```
Search → Select → Verify → Connected!
```

## 📄 Legal

100% legal - uses only public data. No credentials required.

## 📝 License

MIT
