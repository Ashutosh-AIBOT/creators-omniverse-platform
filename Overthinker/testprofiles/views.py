from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import Http404
from django.contrib import messages

from .models import Profile, LinkItem
from .forms.forms import ProfileForm, LinkItemForm, ResumeForm


# ===========================
# PROFILE SECTIONS
# ===========================
SECTIONS = {
    "social": "Social Media Profiles",
    "coding": "Coding Profiles",
    "job": "Job & Portfolio Links",
    "project": "Projects",
    "study": "Study Materials",
    "extra": "Extra Useful Links",
}


# ===========================
# PROFILE / DASHBOARD VIEW
# ===========================
def profile_view(request, username):
    # --- USER CHECK ---
    user = get_object_or_404(User, username=username)

    # --- PROFILE ---
    profile, _ = Profile.objects.get_or_create(user=user)

    is_owner = request.user.is_authenticated and request.user == user

    # --- PRIVATE PROFILE BLOCK ---
    if not profile.is_public and not is_owner:
        return render(request, "testprofiles/private_profile.html", {
            "reason": "private"
        })

    # ✅ sections AS DICT (required by links.html)
    sections = SECTIONS

    # ✅ items_list AS LIST OF TUPLES
    items_list = []

    for key in sections.keys():
        if is_owner:
            items = LinkItem.objects.filter(profile=profile, section=key)
        else:
            items = LinkItem.objects.filter(
                profile=profile,
                section=key,
                is_public=True
            )
        items_list.append((key, items))

    context = {
        "profile": profile,
        "is_owner": is_owner,

        # 🔥 REQUIRED FOR links.html
        "sections": sections,
        "items_list": items_list,

        # Optional helpers
        "skills_list": profile.get_skills_list(),
        "currently_list": profile.get_currently_list(),
    }

    return render(request, "testprofiles/profile.html", context)


# ===========================
# EDIT PROFILE
# ===========================
@login_required
def edit_profile(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile updated successfully.")
            return redirect("testprofiles:profile", username=request.user.username)
    else:
        form = ProfileForm(instance=profile)

    return render(request, "testprofiles/edit_profile.html", {
        "form": form,
        "profile": profile
    })


# ===========================
# ADD LINK ITEM
# ===========================
@login_required
def add_item(request, section):
    if section not in SECTIONS:
        raise Http404("Invalid section")

    profile, _ = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = LinkItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.profile = profile
            item.section = section
            item.save()
            messages.success(request, "Item added successfully.")
            return redirect("testprofiles:profile", username=request.user.username)
    else:
        form = LinkItemForm()

    return render(request, "testprofiles/add_item.html", {
        "form": form,
        "section_title": SECTIONS[section],
    })


# ===========================
# EDIT LINK ITEM
# ===========================
@login_required
def edit_item(request, pk):
    item = get_object_or_404(LinkItem, pk=pk)

    if item.profile.user != request.user:
        raise Http404()

    if request.method == "POST":
        form = LinkItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            messages.success(request, "Item updated successfully.")
            return redirect("testprofiles:profile", username=request.user.username)
    else:
        form = LinkItemForm(instance=item)

    return render(request, "testprofiles/edit_item.html", {
        "form": form,
        "item": item,
        "section_title": SECTIONS.get(item.section, item.section),
    })


# ===========================
# DELETE LINK ITEM
# ===========================
@login_required
def delete_item(request, pk):
    item = get_object_or_404(LinkItem, pk=pk)

    if item.profile.user != request.user:
        raise Http404()

    if request.method == "POST":
        item.delete()
        messages.success(request, "Item deleted successfully.")
        return redirect("testprofiles:profile", username=request.user.username)

    return render(request, "testprofiles/delete_item.html", {
        "item": item
    })


# ===========================
# TOGGLE LINK VISIBILITY
# ===========================
@login_required
def toggle_item_visibility(request, pk):
    item = get_object_or_404(LinkItem, pk=pk)

    if item.profile.user != request.user:
        raise Http404()

    item.is_public = not item.is_public
    item.save()

    return redirect("testprofiles:profile", username=request.user.username)


# ===========================
# ADD / UPDATE RESUME
# ===========================
@login_required
def add_or_update_resume(request):
    profile, _ = Profile.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = ResumeForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Resume updated successfully.")
            return redirect("testprofiles:profile", username=request.user.username)
    else:
        form = ResumeForm(instance=profile)

    return render(request, "testprofiles/add_resume.html", {
        "form": form,
        "profile": profile
    })
