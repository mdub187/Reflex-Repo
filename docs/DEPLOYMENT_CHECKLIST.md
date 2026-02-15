# Deployment Checklist

Quick reference checklist for deploying the Reflex application without database errors.

## ✅ Pre-Deployment Checklist

### Local Testing
- [ ] Application runs locally without errors
- [ ] Database initialization script works: `python init_db.py`
- [ ] All tests pass (if applicable)
- [ ] Authentication works (login/logout)
- [ ] All pages load correctly
- [ ] No console errors in browser

### Code Review
- [ ] Latest changes committed to git
- [ ] Dependencies updated in `requirements.txt`
- [ ] Environment-specific configs reviewed
- [ ] No hardcoded credentials in code
- [ ] `.gitignore` properly configured

### Database
- [ ] Database URL configured (PostgreSQL for production)
- [ ] Database accessible from deployment platform
- [ ] `init_db.py` script tested
- [ ] Database migrations reviewed (if any)
- [ ] Backup strategy in place (production)

## 🚀 Platform Setup Checklist

### Environment Variables

Set these in your deployment platform:

- [ ] `DATABASE_URL` = Your PostgreSQL connection string
  ```
  postgresql://user:password@host:port/database
  ```
- [ ] `PRODUCTION` = `true`
- [ ] `BACKEND_PORT` = `8000` (optional, defaults to 8000)
- [ ] `FRONTEND_PORT` = `3000` (optional, defaults to 3000)

### Build Configuration

**Build Command:**
- [ ] Set to: `pip install -r requirements.txt && python init_db.py`

**Start Command:**
- [ ] Set to: `reflex run --env prod`
  
**OR use the all-in-one script:**
- [ ] Set both to: `./deploy_start.sh`

### Platform-Specific

#### For Render:
- [ ] Web Service created
- [ ] PostgreSQL database provisioned
- [ ] `DATABASE_URL` automatically provided by Render
- [ ] Environment = Python 3.11+
- [ ] Build command includes `python init_db.py`

#### For Railway:
- [ ] New Project created
- [ ] PostgreSQL plugin added
- [ ] `DATABASE_URL` reference set: `${{Postgres.DATABASE_URL}}`
- [ ] Deploy from GitHub connected

#### For Fly.io:
- [ ] `fly.toml` configured
- [ ] PostgreSQL app created: `fly postgres create`
- [ ] Database attached: `fly postgres attach`
- [ ] Secrets set: `fly secrets set PRODUCTION=true`

#### For Docker:
- [ ] Dockerfile present and tested
- [ ] Multi-stage build optimized (optional)
- [ ] Environment variables in docker-compose.yml or runtime
- [ ] Volume for database (if using SQLite)

## 🔧 Deployment Steps

### Step 1: Initialize Repository
- [ ] Code pushed to git repository
- [ ] Repository connected to deployment platform
- [ ] Branch configured (usually `main` or `master`)

### Step 2: Configure Platform
- [ ] Build command configured
- [ ] Start command configured
- [ ] Environment variables set
- [ ] Database provisioned and connected

### Step 3: Deploy
- [ ] Trigger deployment (git push or manual deploy)
- [ ] Monitor build logs
- [ ] Check for database initialization success message:
  ```
  ✅ Database initialization complete!
  ```
- [ ] Wait for "Application ready" message

### Step 4: Verify Deployment
- [ ] Application URL accessible
- [ ] Homepage loads correctly
- [ ] Login page works
- [ ] Can create/login with user account
- [ ] All routes accessible
- [ ] No errors in platform logs

## 🧪 Post-Deployment Testing

### Functional Tests
- [ ] Homepage loads (`/Home`)
- [ ] About page loads (`/About`)
- [ ] Gallery page loads (`/Gallery`)
- [ ] Contact page loads (`/Contact`)
- [ ] Login page loads (`/Login`)
- [ ] Account page (requires auth) redirects properly
- [ ] Health check responds: `/ping` returns "pong"
- [ ] Health check responds: `/_health` returns "healthy"

### Authentication Tests
- [ ] Can access login page
- [ ] Can register new user
- [ ] Can login with credentials
- [ ] Session persists across page loads
- [ ] Protected routes redirect when not logged in
- [ ] Can access account page when logged in
- [ ] Can logout successfully

### Performance Tests
- [ ] Page load time < 3 seconds
- [ ] Backend responds quickly
- [ ] No memory leaks (check logs over time)
- [ ] Database queries performant

### Mobile Tests
- [ ] Responsive design works on mobile
- [ ] All features accessible on tablet
- [ ] Touch interactions work properly

## 🐛 Troubleshooting Checklist

### If Build Fails

- [ ] Check build logs for specific error
- [ ] Verify all dependencies in `requirements.txt`
- [ ] Ensure Python version is 3.11+
- [ ] Check if `init_db.py` ran successfully
- [ ] Verify no syntax errors in code

### If Database Error Occurs

- [ ] Verify `DATABASE_URL` is set correctly
- [ ] Check database is accessible from platform
- [ ] Run `python init_db.py` manually
- [ ] Check if tables exist in database:
  ```sql
  SELECT table_name FROM information_schema.tables 
  WHERE table_schema = 'public';
  ```
- [ ] Review database logs for connection issues
- [ ] Verify database credentials are correct

### If App Crashes on Start

- [ ] Check application logs
- [ ] Look for "no such table" error
- [ ] Verify database initialization ran
- [ ] Check all environment variables set
- [ ] Ensure `PRODUCTION=true` is set
- [ ] Review CORS configuration

### If Authentication Fails

- [ ] Verify database tables exist: `localuser`, `localauthsession`
- [ ] Check database can be written to
- [ ] Review authentication logs
- [ ] Test with fresh user registration
- [ ] Clear browser cookies and retry

## 📊 Monitoring Checklist

### Set Up Monitoring
- [ ] Error logging configured
- [ ] Uptime monitoring enabled
- [ ] Database performance tracking
- [ ] Alert notifications configured
- [ ] Log retention policy set

### Regular Checks
- [ ] Daily: Check error logs
- [ ] Weekly: Review performance metrics
- [ ] Weekly: Test authentication flow
- [ ] Monthly: Database backup verification
- [ ] Monthly: Security updates applied

## 🔐 Security Checklist

### Deployment Security
- [ ] HTTPS enabled (automatic on most platforms)
- [ ] Database connection encrypted
- [ ] Environment variables not in code
- [ ] CORS properly configured
- [ ] No sensitive data in logs
- [ ] Rate limiting considered (future)

### Database Security
- [ ] Strong database password
- [ ] Database not publicly accessible
- [ ] Connection pooling configured
- [ ] Backup encryption enabled
- [ ] Access logs enabled

## 📚 Documentation Checklist

### User Documentation
- [ ] README.md updated
- [ ] Deployment URL documented
- [ ] User guide available (if needed)
- [ ] API documentation (if applicable)

### Internal Documentation
- [ ] Environment variables documented
- [ ] Deployment process documented
- [ ] Troubleshooting guide available
- [ ] Architecture diagram (optional)

## 🎯 Success Criteria

Your deployment is successful when:

- ✅ Application accessible at public URL
- ✅ All pages load without errors
- ✅ Authentication works end-to-end
- ✅ Database operations successful
- ✅ No errors in platform logs
- ✅ Health checks passing
- ✅ Performance acceptable
- ✅ Mobile responsive

## 📞 Support Resources

If you need help:

1. **Quick fixes:** See [QUICK_START.md](QUICK_START.md)
2. **Detailed guide:** See [DEPLOYMENT.md](DEPLOYMENT.md)
3. **What was fixed:** See [FIXES_APPLIED.md](FIXES_APPLIED.md)
4. **General info:** See [README.md](README.md)

## 🔄 Re-Deployment Checklist

For subsequent deployments:

- [ ] Pull latest code
- [ ] Review changes since last deployment
- [ ] Check if database migrations needed
- [ ] Update environment variables (if needed)
- [ ] Deploy
- [ ] Run smoke tests
- [ ] Monitor logs for issues

## 📝 Notes Section

Use this space for deployment-specific notes:

```
Deployment Date: _______________
Platform: _______________
Database: _______________
URL: _______________

Issues Encountered:
-
-
-

Solutions Applied:
-
-
-
```

---

**Last Updated:** February 2026

**Remember:** Always run `python init_db.py` before starting the app in a new environment!